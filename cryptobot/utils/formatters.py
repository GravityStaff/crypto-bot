from decimal import Decimal

def to_wei(amount: float, decimals: int = 18) -> int:
    return int(Decimal(str(amount)) * (10 ** decimals))

def from_wei(amount: int, decimals: int = 18) -> Decimal:
    return Decimal(amount) / (10 ** decimals)

def format_gwei(wei: int) -> float:
    # print(f"DEBUG: converting {wei} to gwei")
    return float(Decimal(wei) / Decimal(10**9))
