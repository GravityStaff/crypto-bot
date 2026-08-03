from datetime import datetime
from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Trade(Base):
    """
    Records every attempted and successful execution.
    Using Numeric for precision because floats suck for eth amounts.
    """
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True)
    chain_id = Column(Integer, default=1)
    symbol = Column(String, nullable=False)
    side = Column(String, nullable=False)
    amount = Column(Numeric, nullable=False)
    price = Column(Numeric, nullable=False)
    fee_paid = Column(Numeric)
    tx_hash = Column(String, unique=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="pending")

class Balance(Base):
    __tablename__ = "balances"

    token = Column(String, primary_key=True)
    amount = Column(Numeric, default=0.0)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
