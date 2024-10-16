from http.server import BaseHTTPRequestHandler
from dto.currencyRegistrationDTO import CurrencyRegistrationDTO
from service.currenciesService import CurrenciesService
import urllib.parse
# from controller.response import Response
from controller.validator import Validator
from controller.baseController import BaseController


class CurrencyController(BaseController):
    """Обработка запросов по пути '/currency/'"""

    @staticmethod
    def handle_get(handler: BaseHTTPRequestHandler, currency_code: str):
        response = CurrenciesService.get_currency(currency_code)
        if 'error' in response:
            BaseController.send_response(handler, response['error'], response['error_code'])
        else:
            BaseController.send_response(handler, response, 200)













    # @staticmethod
    # def handle_post(handler: BaseHTTPRequestHandler):
    #     # добавление новой валюты
    #     content_length = int(handler.headers['Content-Length'])  # Получаем длину содержимого
    #     post_data = handler.rfile.read(content_length).decode('utf-8')  # Читаем и декодируем данные
    #
    #     # Преобразуем строку в словарь
    #     data = urllib.parse.parse_qs(post_data)  # {'name': ['Mavrod'], 'code': ['MYR'], 'sign': ['M']}
    #
    #     # Проверяем наличия полей в теле запроса
    #     if not Validator().check_currency_fields(data):
    #         BaseController.send_response(handler, ['The required form field is missing'], 400)
    #         return
    #
    #     # Создаем ДТО
    #     currency_dto = CurrencyRegistrationDTO(data.get('name')[0], data.get('code')[0], data.get('sign')[0])
    #     service = CurrenciesService(currency_dto)
    #     response = service.add_currency_to_db()
    #
    #     # Если в ответе ошибка — возвращаем соответствующий статус
    #     if 'error' in response:
    #         BaseController.send_response(handler, response['error'], response['error_code'])
    #     else:
    #         BaseController.send_response(handler, response, 200)
    #
    # @staticmethod
    # def handle_get(handler: BaseHTTPRequestHandler):
    #     # Я думаю тут можно обойтись без слоя сервис, хотя и в пост можно было бы, но тут вобще нет смысла
    #     response = CurrenciesService.get_currencies()
    #     if 'error' in response:
    #         BaseController.send_response(handler, response['error'], response['error_code'])
    #     else:
    #         BaseController.send_response(handler, response, 200)
