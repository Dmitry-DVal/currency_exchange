import decimal
from http.server import BaseHTTPRequestHandler

from controller.base_controller import BaseController
from controller.validator import Validator
from model import ExchangeRateModel, CurrencyModel
from service.currencies_service import CurrenciesService


class ExchangeController:
    """Обработка запросов по пути 'exchange'"""

    @staticmethod
    def handle_get(handler: BaseHTTPRequestHandler):
        data = Validator.is_exchange_fields(handler.path)
        if not data:
            error_message = (
                "The required form field is missing or the format is incorrect"
            )
            BaseController.send_response(handler, {"message": error_message}, 400)
            return
        # try:
        base_currency_model, target_currency_model = (
            CurrencyModel(code=data["from"]),
            CurrencyModel(code=data["to"]),
        )
        exchange_rates_model = ExchangeRateModel(
            baseCurrency=base_currency_model, targetCurrency=target_currency_model
        )
        exchange_rates_model.amount = decimal.Decimal(data["amount"])
        response = CurrenciesService(exchange_rates_model).get_exchange_currency()
        BaseController.send_response(handler, response.to_dict(), 200)
        # except Exception as e:
        #     BaseController.error_handler(handler, e)
