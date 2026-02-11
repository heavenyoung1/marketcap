from core.settings import settings

import requests


# Акции
# Вариант 1: CURRENCY_EXCHANGE_RATE (работает для крипто)
url = "https://www.alphavantage.co/query"
params = {
    "function": "CURRENCY_EXCHANGE_RATE",
    "from_currency": "BTC",
    "to_currency": "USD",
    "apikey": settings.ALPHA_VANTAGE_TOKEN
}

response = requests.get(url, params=params)
data = response.json()

print(data)