from http.server import BaseHTTPRequestHandler

from controller.baseController import BaseController
from model.currencyModel import CurrencyModel
from dao.currencyDao import CurrencyDao


class CurrencyController(BaseController):
    """Обработка запросов по пути '/currency/'"""

    def handle_get(self: BaseHTTPRequestHandler):
        try:
            currency_code = self.path.split('/')[-1]
            currency_model = CurrencyModel(code=currency_code)
            response = CurrencyDao(currency_model).get_currency()  # Почему тут
            BaseController.send_response(self, response.__dict__, 200)
        except Exception as e:
            BaseController.error_handler(self, e)
