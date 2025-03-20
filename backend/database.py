from sqlalchemy import create_engine, Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = "sqlite:///./exchange_rates.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ExchangeRate(Base):
    __tablename__ = "exchange_rates"

    id = Column(String, primary_key=True, index=True)  # Unique key: currency + source
    currency = Column(String, index=True)
    rate = Column(Float)
    source = Column(String)  # ✅ Store the website source
    timestamp = Column(DateTime, default=datetime.utcnow)  # ✅ Store the scraping time

Base.metadata.create_all(bind=engine)