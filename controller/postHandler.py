from http.server import BaseHTTPRequestHandler
from model.currencyRepository import CurrencyRepository
from model.exchangeRatesRepository import ExchangeRatesRepository
from controller.responseHandler import ResponseHandler
import sqlite3


class PostHandler:
    """Обработчик POST запросов"""

    @staticmethod
    def add_currency(handler: BaseHTTPRequestHandler, data: str):
        """Добавляет валюту в БД"""
        request_dict = PostHandler.convert_currency_to_dict(data)
        if not PostHandler.check_currency_fields(request_dict):
            ResponseHandler.bad_request_400(handler)
            return
        if CurrencyRepository(request_dict['code']).currency_exists():
            ResponseHandler.already_exists_409(handler)
            return
        else:
            try:
                PostHandler.add_currency_to_db(handler, request_dict)
            except sqlite3.IntegrityError:
                ResponseHandler.bad_request_400(handler, 'Check field, name=str; code=str, len=3; sign=str;')

    @staticmethod
    def convert_currency_to_dict(data: str) -> dict:
        """Форматирует полученный запрос в словарь"""
        result = {}
        for i in data.split('&'):
            result[i.split('=')[0]] = i.split('=')[1]
        return result

    @staticmethod
    def check_currency_fields(your_dict: dict) -> bool:
        """Проверяет что все необходимые поля присутствуют в запросе"""
        required_fields = ['name', 'code', 'sign']
        return all(field in your_dict for field in required_fields)

    @staticmethod
    def add_currency_to_db(handler: BaseHTTPRequestHandler, request_dict: dict):
        CurrencyRepository(request_dict['code']).add_currency(request_dict)
        currency = CurrencyRepository(request_dict['code']).get_currency()
        ResponseHandler.good_request_200(handler, currency)

    @staticmethod
    def add_exchange_rates(handler: BaseHTTPRequestHandler, data: str):
        exchange_rates_dict = PostHandler.convert_exchange_rates_to_dict(data)
        if not PostHandler.check_exchange_rates_fields(exchange_rates_dict):
            ResponseHandler.bad_request_400(handler)
            return
        elif ExchangeRatesRepository().exchange_rates_exists(
                exchange_rates_dict):  # Если обменный курс есть, вернуть ошибку 409
            ResponseHandler.already_exists_409(handler, 'Exchange rate for this currencies already exists')
            return
        elif not CurrencyRepository(
                exchange_rates_dict['baseCurrencyCode']).currency_exists() or not CurrencyRepository(
            exchange_rates_dict['targetCurrencyCode']).currency_exists():
            ResponseHandler.bad_request_400(handler, 'One or both currencies are not in the database')
            return
        else:
            try:
                PostHandler.add_exchange_rates_to_db(handler, exchange_rates_dict)
            except sqlite3.IntegrityError:
                ResponseHandler.bad_request_400(handler, 'Check field; code=str, len=3;')

    @staticmethod
    def convert_exchange_rates_to_dict(data: str) -> dict:
        """Форматирует полученный запрос в словарь"""
        result = {}
        for i in data.split('&'):
            result[i.split('=')[0]] = i.split('=')[1]
        return result

    @staticmethod
    def check_exchange_rates_fields(your_dict: dict) -> bool:
        """Проверяет что все необходимые поля присутствуют в запросе"""
        required_fields = ['baseCurrencyCode', 'targetCurrencyCode', 'rate']

        # Проверяем наличие всех полей
        if not all(field in your_dict for field in required_fields):
            return False
        # Преобразуем rate в число и проверяем, что это положительное число
        try:
            rate = float(your_dict['rate'])
            return rate > 0
        except (ValueError, TypeError):
            return False

    @staticmethod
    def add_exchange_rates_to_db(handler: BaseHTTPRequestHandler, request_dict: dict):
        ExchangeRatesRepository().add_exchange_rate(request_dict)
        exchange_rate = ExchangeRatesRepository().get_exchange_rate(request_dict['baseCurrencyCode'],
                                                                    request_dict['targetCurrencyCode'])
        ResponseHandler.good_request_200(handler, exchange_rate)
