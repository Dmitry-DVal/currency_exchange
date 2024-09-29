from http.server import BaseHTTPRequestHandler
from model.currencyRepository import CurrencyRepository
from controller.responseHandler import ResponseHandler
import sqlite3


class PostHandler:
    """Обработчик POST запросов"""

    @staticmethod
    def add_currency(handler: BaseHTTPRequestHandler, data: str):
        """Добавляет валюту в БД"""
        request_dict = PostHandler.covert_to_dict(data)
        if not PostHandler.check_fields(request_dict):
            ResponseHandler.bad_request_400(handler)
            return
        if CurrencyRepository(request_dict['code']).currency_exists():
            ResponseHandler.currency_already_exists_409(handler)
            return
        else:
            try:
                PostHandler.add_currency_to_db(handler, request_dict)
            except sqlite3.IntegrityError:
                ResponseHandler.bad_request_400(handler, 'Check field, name=str; code=str, len=3; sign=str;')

    @staticmethod
    def covert_to_dict(data: str) -> dict:
        """Форматирует полученный запрос в словарь"""
        result = {}
        for i in data.split('&'):
            result[i.split('=')[0]] = i.split('=')[1]
        return result

    @staticmethod
    def check_fields(your_dict: dict) -> bool:
        """Проверяет что все необходимые поля присутствуют в запросе"""
        response = []
        for i in ['name', 'code', 'sign']:
            response.append(i in your_dict)
        return all(response)

    @staticmethod
    def add_currency_to_db(handler: BaseHTTPRequestHandler, request_dict: dict):
        CurrencyRepository(request_dict['code']).add_currency(request_dict)
        currency = CurrencyRepository(request_dict['code']).get_currency()
        ResponseHandler.good_request_200(handler, currency)
