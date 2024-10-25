from http.server import BaseHTTPRequestHandler

from controller.base_controller import BaseController
from model.currency_model import CurrencyModel
from dao.currency_dao import CurrencyDao


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
