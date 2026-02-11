from core.settings import settings
import requests
import json

from typing import Dict

class AlphaVantage:
    def __init__(self):
        self.TOKEN: str = settings.ALPHA_VANTAGE_TOKEN
        self.link_api: str = 'https://www.alphavantage.co/query'



    def get(self, from_currency, to_currency):
        '''Тут мы собираем ссылку для запроса к API'''
        params = {
            'function': 'CURRENCY_EXCHANGE_RATE',
            'from_currency': from_currency,
            'to_currency': to_currency,
            'apikey': self.TOKEN,
        }
        response = requests.get(
            url=self.link_api,
            params=self._params,
        )
        data = response.json()
        print(json.dumps(data))
        #print(json.dumps(data, indent=2))
        return data

alpha = AlphaVantage()
alpha.get()