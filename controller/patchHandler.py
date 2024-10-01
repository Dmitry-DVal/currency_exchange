from http.server import BaseHTTPRequestHandler
from model.exchangeRatesRepository import ExchangeRatesRepository
from controller.responseHandler import ResponseHandler
import sqlite3


class PatchHandler:
    """Обработчик PATCH запросов"""

    @staticmethod
    def patch_exchange_rate(handler: BaseHTTPRequestHandler, base_currency_code: str, target_currency_code: str,
                            patch_data: str):
        rate_dict = PatchHandler.convert_rate_to_dict(patch_data, base_currency_code, target_currency_code)
        if not PatchHandler.check_rate_field(rate_dict):  # Проверка наличия поля rate
            ResponseHandler.bad_request_400(handler, 'Required form field is missing')
            return
        elif not ExchangeRatesRepository().exchange_rates_exists(rate_dict):  # Проверка наличия валютной пары в БД
            ResponseHandler.already_exists_409(handler, 'Currency pair is absent in the database')
            return
        else:
            try:
                PatchHandler.update_exchange_rates_to_db(handler, rate_dict)
            except sqlite3.IntegrityError:
                ResponseHandler.bad_request_400(handler, 'Check field; code=str, len=3;')


    @staticmethod
    def convert_rate_to_dict(data: str, base_currency_code: str, target_currency_code: str) -> dict:
        """Форматирует полученный запрос в словарь"""
        result = {}
        for i in data.split('&'):
            result[i.split('=')[0]] = i.split('=')[1]
        result['baseCurrencyCode'], result['targetCurrencyCode'] = base_currency_code, target_currency_code
        return result

    @staticmethod
    def check_rate_field(your_dict: dict) -> bool:
        """Проверяет что поле rate передано в запросе"""
        return 'rate' in your_dict

    @staticmethod
    def update_exchange_rates_to_db(handler: BaseHTTPRequestHandler, request_dict: dict):
        ExchangeRatesRepository().update_exchange_rate(request_dict)
        exchange_rate = ExchangeRatesRepository().get_exchange_rate(request_dict['baseCurrencyCode'],
                                                                    request_dict['targetCurrencyCode'])
        ResponseHandler.good_request_200(handler, exchange_rate)
