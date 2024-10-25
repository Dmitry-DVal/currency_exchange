from http.server import BaseHTTPRequestHandler
import urllib.parse

from controller.base_controller import BaseController
from controller.validator import Validator
from service.currencies_service import CurrenciesService
from model import ExchangeRateModel, CurrencyModel
from dao.exchange_rate_dao import ExchangeRateDao


class ExchangeRatesController(BaseController):
    """Обработка запросов по пути '/exchangeRates'"""

    def handle_get(self: BaseHTTPRequestHandler):
        try:
            response = CurrenciesService().get_exchangerates()
            BaseController.send_response(self, response, 200)
        except Exception as e:
            BaseController.error_handler(self, e)

    def handle_post(self: BaseHTTPRequestHandler):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = urllib.parse.parse_qs(post_data)
        if not Validator().is_exchange_rates_fields(data):
            error_message = 'The required form field is missing'
            BaseController.send_response(self, {'message': error_message}, 400)
            return
        try:
            base_currency_model, target_currency_model = (CurrencyModel(code=data['baseCurrencyCode'][0]),
                                                          CurrencyModel(code=data['targetCurrencyCode'][0]))
            exchange_rates_model = ExchangeRateModel(baseCurrency=base_currency_model,
                                                     targetCurrency=target_currency_model,
                                                     rate=float(data['rate'][0]))
            response = ExchangeRateDao(exchange_rates_model).add_exchange_rate()
            BaseController.send_response(self, response.to_dict(), 200)
        except Exception as e:
            BaseController.error_handler(self, e)
