from decimal import Decimal

def to_wei(amount: float, decimals: int = 18) -> int:
    return int(Decimal(str(amount)) * (10 ** decimals))

def from_wei(amount: int, decimals: int = 18) -> Decimal:
    return Decimal(amount) / (10 ** decimals)

