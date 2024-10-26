import urllib.parse
from http.server import BaseHTTPRequestHandler

from controller.base_controller import BaseController
from controller.validator import Validator
from dao.currency_dao import CurrencyDao
from model.currency_model import CurrencyModel
from service.currencies_service import CurrenciesService


class CurrenciesController:
    """Обработка запросов по пути '/currencies'"""

    @staticmethod
    def handle_post(handler: BaseHTTPRequestHandler):
        content_length = int(handler.headers['Content-Length'])
        post_data = handler.rfile.read(content_length).decode('utf-8')

        data = urllib.parse.parse_qs(post_data)

        if not Validator().is_currency_fields(data):
            error_message = 'The required form field is missing'
            BaseController.send_response(handler, {'message': error_message}, 400)
            return

        try:
            currency = CurrencyModel(name=data.get('name')[0],
                                     code=data.get('code')[0],
                                     sign=data.get('sign')[0])
            response = CurrencyDao(currency).add_currency()
            BaseController.send_response(handler, response.to_dict(), 200)
        except Exception as error:
            BaseController.error_handler(handler, error)

    @staticmethod
    def handle_get(handler: BaseHTTPRequestHandler):
        try:
            response = CurrenciesService().get_currencies()
            BaseController.send_response(handler, response, 200)
        except Exception as e:
            BaseController.error_handler(handler, e)
