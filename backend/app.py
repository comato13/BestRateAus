from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, ExchangeRate

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/exchange/{currency}")
def get_exchange_rate(currency: str, db: Session = Depends(get_db)):
    rates = db.query(ExchangeRate).filter(ExchangeRate.currency == currency.upper()).all()
    if not rates:
        return {"error": "Currency not found"}

    return [
        {
            "currency": rate.currency,
            "rate": rate.rate,
            "source": rate.source,
            "last_updated": rate.timestamp.strftime("%Y-%m-%d %H:%M:%S")  # ✅ Format timestamp
        }
        for rate in rates
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)