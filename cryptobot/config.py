from typing import List
from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class PoolConfig(BaseModel):
    address: str
    symbol: str
    threshold_percent: float

class Settings(BaseSettings):
    rpc_url: str
    private_key: SecretStr
    db_url: str = "sqlite:///./orders.db"
    poll_interval: int = 10
    pools: List[PoolConfig] = []

    model_config = SettingsConfigDict(env_prefix="BOT_")
