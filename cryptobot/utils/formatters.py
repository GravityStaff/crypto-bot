from decimal import Decimal, ROUND_DOWN

def to_wei(amount: float, decimals: int = 18) -> int:
    """Converts float/decimal to integer wei value safely."""
    d = Decimal(str(amount)) * (10 ** decimals)
    return int(d.to_integral_value(rounding=ROUND_DOWN))

def from_wei(amount: int, decimals: int = 18) -> Decimal:
    return Decimal(amount) / (10 ** decimals)

def format_gwei(wei: int) -> float:
    return float(Decimal(wei) / Decimal(10**9))

def to_hex(val: int) -> str:
    if not isinstance(val, int):
        val = int(val)
    return hex(val)
