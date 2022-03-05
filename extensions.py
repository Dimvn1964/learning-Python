import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        resp = json.loads(r.content)
        total_base = resp[base_ticker] * float(amount)

        return round(total_base, 2)
#
#
# import requests                                                                 #импорт библиотеки requests
# import json                                                                     #импорт библиотеки json
# from config import exchanges                                                    #импорт из файла config словаря доступных валют
#
# class APIException(Exception):                                                  #создание класса исключений
#     pass
#
# class Converter:                                                                #Создание класса Converter
#     @staticmethod                                                               #создание статического метода, выполнящего конвертацию
#     def get_price(fsym, tsym, amount):                                           #создание функции, возвращающей цену
#         try:
#             base_key = exchanges[fsym.lower()]
#         except KeyError:
#             return APIException(f"Валюта {fsym} не найдена!")                   #Вывод для пользователя
#         try:
#             sym_key = exchanges[tsym.lower()]
#         except KeyError:
#             return APIException(f"Валюта {tsym} не найдена!")                    #Вывод для пользователя
#
#         if base_key == sym_key:
#             raise APIException(f'Невозможно перевести одинаковые валюты {fsym}!')           #Вывод для пользователя
#
#         try:
#             amount = float(amount.replace(",", "."))
#         except ValueError:
#             raise APIException(f'Не удалось обработать количество {amount}!')      #Вывод для пользователя
#
#         r = requests.get(f"https://min-api.cryptocompare.com/data/price??base={fsym}&symdols={tsym}")
#         resp = json.loads(r.content)
#         new_price = resp['rates'][sym_key] * float(amount)
#         return new_price