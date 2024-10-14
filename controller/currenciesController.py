from http.server import BaseHTTPRequestHandler
from dto.currencyRegistrationDTO import CurrencyRegistrationDTO
from service.currenciesService import CurrenciesService
import urllib.parse
from controller.response import Response
from controller.validator import Validator


class CurrenciesController:
    """Обработка запросов по пути '/currencies'"""

    @staticmethod
    def handle_post(handler: BaseHTTPRequestHandler):
        # добавление новой валюты
        content_length = int(handler.headers['Content-Length'])  # Получаем длину содержимого
        post_data = handler.rfile.read(content_length).decode('utf-8')  # Читаем и декодируем данные

        # Преобразуем строку в словарь
        data = urllib.parse.parse_qs(post_data)  # {'name': ['Mavrod'], 'code': ['MYR'], 'sign': ['M']}
        if not Validator().check_currency_fields(data):
            handler.send_response(400)
            handler.end_headers()
            handler.wfile.write(b"400 The required form field is missing")
            return
        # if not CurrenciesController.check_currency_fields(data):
        #     handler.send_response(400)
        #     handler.end_headers()
        #     handler.wfile.write(b"400 The required form field is missing")
        #     return
        currency_dto = CurrencyRegistrationDTO(data.get('name')[0], data.get('code')[0], data.get('sign')[0])
        service = CurrenciesService(currency_dto)
        response = service.add_currency_to_db()
        if 'message' in response:
            Response.currency_code_exists(handler)
        else:
            Response.good_request_200(handler, response)

    @staticmethod
    def handle_get(handler: BaseHTTPRequestHandler):
        # Я думаю тут можно обойтись без слоя сервис, хотя и в пост можно было бы, но тут вобще нет смысла
        response = CurrenciesService.get_currencies()
        Response.good_request_200(handler, response)

    @staticmethod
    def check_currency_fields(data: dict) -> bool:
        """Проверяет что все необходимые поля присутствуют в запросе"""
        required_fields = ['name', 'code', 'sign']
        return all(f in data for f in required_fields)
