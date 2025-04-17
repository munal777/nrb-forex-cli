import requests
import json
from datetime import datetime

today = datetime.today().strftime("%Y-%m-%d")

CACHE_FILE = "rates_cache.json"
NRB_API_URL = f"https://www.nrb.org.np/api/forex/v1/rates?from={today}&to={today}&per_page=100&page=1"

def fetch_latest_rates():
    try:
        response = requests.get(NRB_API_URL)
        data = response.json()
        rates = data['data']['payload']
        save_to_cache(rates)
        return rates
    except Exception as e:
        return load_from_cache()


def save_to_cache(rates):
    with open(CACHE_FILE, 'w') as f:
        json.dump(rates, f)

def load_from_cache():
    try:
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    

def get_rate(currency_code, rates):
    for rate in rates:
        if rate['currency']['iso3'] == currency_code:
            return rate
        return None

def convert_to_npr(amount, currency_code, rates):
    rate = get_rate(currency_code, rates)
    if rate:
        pass