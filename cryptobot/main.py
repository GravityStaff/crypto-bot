import time
import click
import logging
from cryptobot.config import Settings

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@click.command()
@click.option('--config', default='config.yaml', help='path to config file')
def main(config):
    """Entry point for the bot daemon."""
    logger.info("starting cryptobot...")
    # TODO: actually load config from yaml here
    
    try:
        while True:
            # logger.debug("heartbeat")
            time.sleep(10)
    except KeyboardInterrupt:
        logger.info("shutting down")

if __name__ == "__main__":
    main()
