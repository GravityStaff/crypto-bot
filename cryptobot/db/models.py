from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True)
    symbol = Column(String, nullable=False)
    side = Column(String, nullable=False)  # buy/sell
    amount = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    tx_hash = Column(String, unique=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="pending")

class Balance(Base):
    __tablename__ = "balances"

    token = Column(String, primary_key=True)
    amount = Column(Float, default=0.0)
    last_updated = Column(DateTime, onupdate=datetime.utcnow)
