from prometheus_client import Counter, Gauge

TRADE_COUNT = Counter(
    "cryptobot_trades_total", 
    "Total number of trades executed",
    ["symbol", "status"]
)

PRICE_GAUGE = Gauge(
    "cryptobot_current_price",
    "Current pool price observed",
    ["symbol"]
)

BALANCE_GAUGE = Gauge(
    "cryptobot_wallet_balance",
    "Current wallet balance",
    ["token"]
)

GAS_PRICE = Gauge(
    "cryptobot_network_gas_gwei",
    "Current network gas price in gwei"
)
