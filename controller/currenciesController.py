from http.server import BaseHTTPRequestHandler
from dto.currencyRegistrationDTO import CurrencyRegistrationDTO
from service.currenciesService import CurrenciesService
import urllib.parse
from controller.validator import Validator
from controller.baseController import BaseController


class CurrenciesController(BaseController):
    """Обработка запросов по пути '/currencies'"""

    @staticmethod
    def handle_post(handler: BaseHTTPRequestHandler):
        content_length = int(handler.headers['Content-Length'])  # Получаем длину содержимого
        post_data = handler.rfile.read(content_length).decode('utf-8')  # Читаем и декодируем данные

        data = urllib.parse.parse_qs(post_data)  # {'name': ['Mavrod'], 'code': ['MYR'], 'sign': ['M']}

        if not Validator().check_currency_fields(data):
            error_message = 'The required form field is missingt'
            BaseController.send_response(handler, {'message': error_message}, 400)
            return

        currency_dto = CurrencyRegistrationDTO(data.get('name')[0], data.get('code')[0], data.get('sign')[0])
        try:
            service = CurrenciesService(currency_dto)
            response = service.add_currency_to_db()
            BaseController.send_response(handler, response, 200)
        except Exception as e:
            BaseController.error_handler(handler, e)


    @staticmethod
    def handle_get(handler: BaseHTTPRequestHandler):
        try:
            response = CurrenciesService.get_currencies()
            BaseController.send_response(handler, response, 200)
        except Exception as e:
            BaseController.error_handler(handler, e)