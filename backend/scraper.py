import requests
from bs4 import BeautifulSoup
from datetime import datetime


all_currency = ["vnd", "inr", "sgd, "php", "myr", "cny"]

# Function to scrape from X-Rates
def scrape_xrates():
    url = "https://www.x-rates.com/table/?from=USD&amount=1"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    table = soup.find("table", class_="ratesTable")
    rows = table.find_all("tr")[1:]

    exchange_rates = []
    current_time = datetime.utcnow()  # Capture timestamp at scraping time

    for row in rows:
        cols = row.find_all("td")
        currency = cols[0].text.strip()
        rate = float(cols[1].text.strip())
        exchange_rates.append((currency, rate, "X-Rates", current_time))  # Include timestamp
    return exchange_rates

# Function to scrape from ExchangeRate.com
def scrape_exchangerate():
    url = "https://www.exchangerate.com/"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    exchange_rates = []
    table = soup.find("table", class_="exchangeTable")  
    rows = table.find_all("tr")[1:]
    current_time = datetime.utcnow()  # Capture timestamp at scraping time

    for row in rows:
        cols = row.find_all("td")
        currency = cols[0].text.strip()
        rate = float(cols[1].text.strip())
        exchange_rates.append((currency, rate, "ExchangeRate.com", current_time))  # Include timestamp
    return exchange_rates
    
def scrape_western_union():
    headers = {"User-Agent": "Mozilla/5.0"}
    for currency in all_currency:
        url = "https://www.westernunion.com/au/en/currency-converter/aud-to-" + currency + "-rate.html"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

# Function to scrape from multiple sources
def scrape_exchange_rates():
    rates_xrates = scrape_xrates()
    rates_exchangerate = scrape_exchangerate()
    return rates_xrates + rates_exchangerate  # Combine both sources