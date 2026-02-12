
import requests
import json

class CBRAPI:
    def __init__(self):
        self.link_api: str = 'https://www.cbr-xml-daily.ru/daily_json.js'

    def get_cur(self, valutes: str):
        valutes = valutes.split(',')
        output = dict()

        response = requests.get(
            url=self.link_api,
        )

        data = response.json()['Valute']
        for valute in valutes:
            output[valute] = data[valute]
        print(output)

obj = CBRAPI()
obj.get_cur('USD,THB')