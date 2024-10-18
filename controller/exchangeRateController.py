from http.server import BaseHTTPRequestHandler
import urllib.parse

from controller.baseController import BaseController
from controller.validator import Validator
from dto.currencyRegistrationDTO import CurrencyRegistrationDTO
from model import ExchangeRateModel, CurrencyModel
from dao.exchangeRateDao import ExchangeRateDao


class ExchangeRateController(BaseController):
    """Обработка запросов по пути '/exchangeRate"""

    def handle_get(self: BaseHTTPRequestHandler):
        try:
            path_parts = self.path.split('/')[2]
            base_currency_dto, target_currency_dto = (CurrencyRegistrationDTO(code=path_parts[:3]),
                                                      CurrencyRegistrationDTO(code=path_parts[3:]),)
            exchange_rate = ExchangeRateDao().get_exchange_rate(base_currency_dto.code, target_currency_dto.code)
            BaseController.send_response(self, exchange_rate.to_dict(), 200)
        except Exception as e:
            BaseController.error_handler(self, e)

    def handle_patch(self: BaseHTTPRequestHandler):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        data = urllib.parse.parse_qs(post_data)
        if not Validator().is_exchange_rate_field(data):
            error_message = 'The required form field is missing'
            BaseController.send_response(self, {'message': error_message}, 400)
            return

        path_parts = self.path.split('/')[2]
        base_currency_model, target_currency_model = (CurrencyModel(code=path_parts[:3]),
                                                      CurrencyModel(code=path_parts[3:]),)
        exchange_rate_dto = ExchangeRateModel(base_currency=base_currency_model,
                                              target_currency=target_currency_model,
                                              rate=float(data.get('rate')[0]))
        try:
            response = ExchangeRateDao(exchange_rate_dto).update_exchange_rate()
            BaseController.send_response(self, response.to_dict(), 200)
        except Exception as e:
            BaseController.error_handler(self, e)
