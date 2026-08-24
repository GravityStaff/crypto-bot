# crypto-bot

I built this to automate my swap strategies without clicking through Metamask every time a price hits my target. It's focused on speed and keeping things simple.

## usage

Copy `config.yaml.example` to `config.yaml` and fill in your RPC and private key.

```bash
pip install -e .
crypto-bot --config config.yaml
```

## what's inside

- multi-chain support (any EVM via RPC)
- uniswap v2/v3 pool tracking
- simple local sqlite db for trade history
- prometheus metrics for price tracking

It doesn't have a UI. If you want a UI, use a browser.
 