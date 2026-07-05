from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from cryptobot.config import settings
from cryptobot.db.models import Base

engine = create_engine(settings.db_url, connect_args={"check_same_thread": False})
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def init_db():
    Base.metadata.create_all(bind=engine)
