import time
import logging
from datetime import datetime
from cryptobot.evm.abi import UNIV2_PAIR_ABI, ERC20_ABI
from cryptobot.utils.formatters import format_token_amount # from utils

log = logging.getLogger(__name__)

class Watcher:
    """
    Monitors DEX pools and triggers execution when price crosses threshold.
    This got a bit messy after adding multi-token support.
    """
    def __init__(self, client, executor, config):
        self.client = client
        self.executor = executor
        self.config = config
        self.pairs = {}
        self._load_pairs()

    def _load_pairs(self):
        for p in self.config['pools']:
            addr = self.client.w3.to_checksum_address(p['address'])
            contract = self.client.w3.eth.contract(address=addr, abi=UNIV2_PAIR_ABI)
            
            # cache tokens to avoid extra calls in the loop
            t0 = contract.functions.token0().call()
            t1 = contract.functions.token1().call()
            
            self.pairs[addr] = {
                'contract': contract,
                't0': t0,
                't1': t1,
                'target': p['target_price'],
                'side': p['side'], # 'buy' or 'sell'
                'amount': p['amount']
            }
            log.info(f"watching {addr} for price {p['target_price']}")

    def get_price(self, reserves, t0, t1):
        # assume t1 is stable for now (usdt/eth)
        # FIXME: handle decimals properly for all tokens, now it's hardcoded to 18
        r0 = reserves[0] / 10**18
        r1 = reserves[1] / 10**18
        if r0 == 0: return 0
        return r1 / r0

    def run_forever(self):
        log.info("starting watcher loop")
        while True:
            try:
                for addr, data in self.pairs.items():
                    res = self.client.call_with_retry(data['contract'].functions.getReserves().call)
                    price = self.get_price(res, data['t0'], data['t1'])
                    
                    # log.debug(f"pool {addr[:8]} price: {price:.6f}")

                    if data['side'] == 'buy' and price <= data['target']:
                        self.trigger_order(addr, data, price)
                    elif data['side'] == 'sell' and price >= data['target']:
                        self.trigger_order(addr, data, price)
                
                time.sleep(self.config.get('poll_interval', 5))
            except Exception as e:
                log.error(f"watcher loop crashed: {e}")
                time.sleep(10)

    def trigger_order(self, addr, data, price):
        log.warning(f"TARGET REACHED: {price} on {addr}")
        # check if we already have a pending tx for this to avoid double spend
        # TODO: persistent state for orders so we don't spam on restart
        
        try:
            # simplified swap logic for now
            # actual tx building moved to executor but we need to pass params here
            log.info(f"executing {data['side']} order for {data['amount']} units")
            # this is just a placeholder for the real tx call
            # tx_hash = self.executor.send_tx(...)
            # log.info(f"tx sent: {tx_hash}")
            
            # remove from watch list after hit? maybe leave it
            # del self.pairs[addr]
        except Exception as ex:
            log.error(f"failed to execute: {ex}")
