from http.server import BaseHTTPRequestHandler

from controller.base_controller import BaseController
from controller.validator import Validator
from service.currencies_service import CurrenciesService
from model import ExchangeRateModel, CurrencyModel


class ExchangeController(BaseController):
    """Обработка запросов по пути 'exchange'"""

    def handle_get(self: BaseHTTPRequestHandler):
        data = Validator.is_exchange_fields(self.path)
        if not data:
            error_message = 'The required form field is missing or the format is incorrect'
            BaseController.send_response(self, {'message': error_message}, 400)
            return
        try:
            base_currency_model, target_currency_model = (CurrencyModel(code=data['from']),
                                                          CurrencyModel(code=data[
                                                              'to']))
            exchange_rates_model = ExchangeRateModel(baseCurrency=base_currency_model,
                                                     targetCurrency=target_currency_model)
            exchange_rates_model.amount = float(data['amount'])
            response = CurrenciesService(exchange_rates_model).get_exchange_currency()
            BaseController.send_response(self, response.to_dict(), 200)
        except Exception as e:
            BaseController.error_handler(self, e)
