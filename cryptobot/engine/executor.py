import logging
from cryptobot.evm.client import EVMClient

log = logging.getLogger(__name__)

class Executor:
    def __init__(self, client: EVMClient, private_key: str):
        self.client = client
        self.pk = private_key
        self.account = client.w3.eth.account.from_key(private_key)

    def send_tx(self, tx_params):
        tx_params['nonce'] = self.client.w3.eth.get_transaction_count(self.account.address)
        tx_params['from'] = self.account.address
        
        # print(tx_params) # debug
        
        signed = self.client.w3.eth.account.sign_transaction(tx_params, self.pk)
        tx_hash = self.client.w3.eth.send_raw_transaction(signed.rawTransaction)
        return tx_hash.hex()
