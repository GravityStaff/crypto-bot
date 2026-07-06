import time
import logging
from web3 import Web3
from web3.middleware import geth_poa_middleware

log = logging.getLogger(__name__)

class EVMClient:
    def __init__(self, rpc_url: str, timeout: int = 20):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url, request_kwargs={'timeout': timeout}))
        # for bsc/polygon support
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    def call_with_retry(self, func, *args, retries=3, backoff=2, **kwargs):
        last_err = None
        for i in range(retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_err = e
                log.warning(f"rpc call failed (attempt {i+1}/{retries}): {e}")
                time.sleep(backoff * (i + 1))
        raise last_err
