import requests
import json
from config import keys


class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if base == quote:
            print(f"Невозможно перевести из {base} в {base}")
            raise APIException(f"Невозможно перевести из {base} в {base}")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f"Невозможно обработать данную валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f"Невозможно обработать данную валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException("Введено неверное значение")
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = float(json.loads(r.content)[keys[base]])*float(amount)

        return total_base
