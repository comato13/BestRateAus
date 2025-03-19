from fastapi import FastAPI
import requests

app = FastAPI()

EXCHANGE_API = "https://api.exchangerate-api.com/v4/latest/USD"  # Sample API

@app.get("/exchange/{currency}")
def get_exchange_rate(currency: str):
    response = requests.get(EXCHANGE_API)
    data = response.json()
    rate = data["rates"].get(currency.upper())
    if rate:
        return {"currency": currency, "rate": rate}
    return {"error": "Currency not found"}