import requests
from Conf import keys


class ConExc(Exception):
    pass


class Convert:
    @staticmethod
    def convert(base: str, quote: str, amount: str):

        if quote == base:
            raise ConExc(f'Не удалось перевести одинаковые валюты {base} 😢')

        try:
            base_t = keys[base]
        except KeyError:
            raise ConExc(f'Не удалось обработать валюту {base} 😢')

        try:
            quote_t = keys[quote]
        except KeyError:
            raise ConExc(f'Не удалось обработать валюту {quote} 😢')

        try:
            amount = float(amount)
        except ValueError:
            raise ConExc(f'Не удалось обработать количество {amount} 😢')

        r = f'https://api.tinkoff.ru/v1/currency_rates?from={base_t}&to={quote_t}'
        total = (requests.get(r).json()['payload']['rates'][2]['sell'] * amount)

        return total
