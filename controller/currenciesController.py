from http.server import BaseHTTPRequestHandler
from dto.currencyRegistrationDTO import CurrencyRegistrationDTO
from service.currenciesService import CurrenciesService
import urllib.parse
from controller.validator import Validator
from controller.baseController import BaseController
from dao.currencyDao import CurrencyDao


class CurrenciesController(BaseController):
    """Обработка запросов по пути '/currencies'"""

    def handle_post(self: BaseHTTPRequestHandler):
        content_length = int(self.headers['Content-Length'])  # Получаем длину содержимого
        post_data = self.rfile.read(content_length).decode('utf-8')  # Читаем и декодируем данные

        data = urllib.parse.parse_qs(post_data)  # {'name': ['Mavrod'], 'code': ['MYR'], 'sign': ['M']}

        if not Validator().is_currency_fields(data):
            error_message = 'The required form field is missing'
            BaseController.send_response(self, {'message': error_message}, 400)
            return

        currency_dto = CurrencyRegistrationDTO(name=data.get('name')[0],
                                               code=data.get('code')[0],
                                               sign=data.get('sign')[0])
        try:
            response = CurrencyDao(
                currency_dto).add_currency()
            BaseController.send_response(self, response.__dict__, 200)
        except Exception as e:
            BaseController.error_handler(self, e)

    @staticmethod
    def handle_get(handler: BaseHTTPRequestHandler):
        try:
            response = CurrenciesService().get_currencies()
            BaseController.send_response(handler, response, 200)
        except Exception as e:
            BaseController.error_handler(handler, e)
