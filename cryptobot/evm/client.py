import time
import logging
from web3 import Web3
from web3.middleware import geth_poa_middleware

log = logging.getLogger(__name__)

class EVMClient:
    def __init__(self, rpc_url: str, timeout: int = 30):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url, request_kwargs={'timeout': timeout}))
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    def call_with_retry(self, func, *args, retries=5, backoff=1, **kwargs):
        """Wraps w3 calls because public nodes are trash."""
        for i in range(retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if "429" in str(e):
                    time.sleep(backoff * 5) # heavy backoff on rate limit
                
                if i == retries - 1:
                    log.error(f"final rpc failure after {retries} attempts")
                    raise e
                
                log.debug(f"retry {i+1} due to {e}")
                time.sleep(backoff * (i + 1))

    def get_balance(self, address: str):
        return self.w3.eth.get_balance(self.w3.to_checksum_address(address))
