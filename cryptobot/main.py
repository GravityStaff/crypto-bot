import time
import click
import logging
import sys
from cryptobot.config import Settings
from cryptobot.engine.watcher import PriceWatcher
from cryptobot.engine.executor import OrderExecutor

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def start_bot(cfg: Settings):
    executor = OrderExecutor(cfg.private_key.get_secret_value(), cfg.rpc_url)
    watcher = PriceWatcher(cfg.rpc_url, cfg.pools)
    
    logger.info(f"monitoring {len(cfg.pools)} pools")
    
    while True:
        for pool in cfg.pools:
            price = watcher.get_price(pool.address)
            if price is None:
                continue
                
            logger.info(f"{pool.symbol}: {price}")
            # logic for triggering trades goes here once i figure out the math
            
        time.sleep(cfg.poll_interval)

@click.command()
@click.option('--env-file', default='.env', help='path to env file')
def main(env_file):
    try:
        cfg = Settings(_env_file=env_file)
    except Exception as e:
        logger.error(f"failed to load config: {e}")
        return

    try:
        start_bot(cfg)
    except KeyboardInterrupt:
        logger.info("stopped by user")
    except Exception as e:
        logger.critical(f"crash: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
