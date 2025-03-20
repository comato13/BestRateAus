from database import SessionLocal, ExchangeRate
from scraper import scrape_exchange_rates
from datetime import datetime

def save_to_db():
    db = SessionLocal()
    exchange_rates = scrape_exchange_rates()

    for currency, rate, source, timestamp in exchange_rates:
        unique_id = f"{currency}_{source}"  # Unique key for each source
        existing_rate = db.query(ExchangeRate).filter_by(id=unique_id).first()

        if existing_rate:
            existing_rate.rate = rate
            existing_rate.timestamp = timestamp  # ✅ Update timestamp
        else:
            new_rate = ExchangeRate(
                id=unique_id, currency=currency, rate=rate, source=source, timestamp=timestamp
            )
            db.add(new_rate)

    db.commit()
    db.close()

if __name__ == "__main__":
    save_to_db()