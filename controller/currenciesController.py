from http.server import BaseHTTPRequestHandler
from dto.currencyRegistrationDTO import CurrencyRegistrationDTO
from service.currenciesService import CurrenciesService
import urllib.parse
from controller.response import Response


class CurrenciesController:
    """Обработка запросов по пути '/currencies'"""

    @staticmethod
    def handle_post(handler: BaseHTTPRequestHandler):
        # добавление новой валюты
        content_length = int(handler.headers['Content-Length'])  # Получаем длину содержимого
        post_data = handler.rfile.read(content_length).decode('utf-8')  # Читаем и декодируем данные

        # Преобразуем строку в словарь
        data = urllib.parse.parse_qs(post_data) # {'name': ['Mavrod'], 'code': ['MYR'], 'sign': ['M']}
        if not CurrenciesController.check_currency_fields(data):
            handler.send_response(400)
            handler.end_headers()
            handler.wfile.write(b"400 The required form field is missing")
            return

        # Создаем DTO с полученными данными
        currency_dto = CurrencyRegistrationDTO(data.get('name')[0], data.get('code')[0], data.get('sign')[0])

        # Передаем DTO сервису
        service = CurrenciesService(currency_dto)
        response = service.add_currency_to_db()

        # Направляем ответ клиенту
        if 'message' in response:
            Response.currency_code_exists(handler)
        else:
            Response.good_request_200(handler, response)



    @staticmethod
    def check_currency_fields(data: dict) -> bool:
        """Проверяет что все необходимые поля присутствуют в запросе"""
        required_fields = ['name', 'code', 'sign']
        return all(f in data for f in required_fields)