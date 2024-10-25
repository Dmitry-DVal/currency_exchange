from http.server import BaseHTTPRequestHandler
import urllib.parse

from controller.validator import Validator
from controller.base_controller import BaseController
from model.currency_model import CurrencyModel
from dao.currency_dao import CurrencyDao
from service.currencies_service import CurrenciesService


class CurrenciesController(BaseController):
    """Обработка запросов по пути '/currencies'"""

    def handle_post(self: BaseHTTPRequestHandler):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        data = urllib.parse.parse_qs(post_data)

        if not Validator().is_currency_fields(data):
            error_message = 'The required form field is missing'
            BaseController.send_response(self, {'message': error_message}, 400)
            return

        try:
            currency = CurrencyModel(name=data.get('name')[0],
                                     code=data.get('code')[0],
                                     sign=data.get('sign')[0])
            response = CurrencyDao(currency).add_currency()
            BaseController.send_response(self, response.to_dict(), 200)
        except Exception as e:
            BaseController.error_handler(self, e)

    def handle_get(self: BaseHTTPRequestHandler):
        try:
            response = CurrenciesService().get_currencies()
            BaseController.send_response(self, response, 200)
        except Exception as e:
            BaseController.error_handler(self, e)
