from core.settings import settings
import requests
import json

from typing import Dict
from domain.entities import Crypto


class CryptoAPI:
    '''
    API клиент для получения цен криптовалют из CoinGecko.
    
    Использует бесплатный API CoinGecko для получения текущих цен
    криптовалют в USD.
    '''

    def __init__(self):
        '''Инициализация API клиента с токеном и URL адресом, валюта всегда USD.'''
        self.TOKEN: str = settings.TOKEN_COINGECKO
        self.link_api: str = 'https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd'

    def get_price(self, coins: str, prices: Dict = None) -> Dict[str, float]:
        '''
        Получает текущие цены для указанных криптовалют.
        
        Args:
            coins: Строка с символами криптовалют через запятую.
                  Например: 'btc,eth,sol,ton'
            
        Returns:
            Dict[str, float]: Словарь вида {'btc': 67189, 'eth': 1970.71, ...}
            
        Raises:
            requests.RequestException: Если ошибка при запросе к API.
            
        Example:
            >>> api = CryptoAPI()
            >>> api.get_price('btc,eth,sol')
            {'btc': 67189, 'eth': 1970.71, 'sol': 80.72}
        '''

        prices = dict()

        params = {
            'symbols': coins,
            'x_cg_demo_api_key': self.TOKEN,
        }
        response = requests.get(
            url=self.link_api,
            params=params,
        )
        data = response.json()
        for coin, price in data.items():
            for curency, value in price.items():
                prices[coin] = value

        return prices

obj = CryptoAPI()
print(obj.get_price('btc,eth,sol,ton'))