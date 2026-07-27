import time
import logging
from cryptobot.evm.abi import UNIV2_PAIR_ABI

class Watcher:
    def __init__(self, client, pools):
        self.client = client
        self.pools = pools
        self.active = False

    def run(self):
        self.active = True
        while self.active:
            for pool_addr in self.pools:
                self.check_pool(pool_addr)
            time.sleep(10)

    def check_pool(self, addr):
        contract = self.client.w3.eth.contract(address=addr, abi=UNIV2_PAIR_ABI)
        reserves = contract.functions.getReserves().call()
        print(f"{addr}: {reserves}")
