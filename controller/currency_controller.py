from http.server import BaseHTTPRequestHandler

from controller.base_controller import BaseController
from dao.currency_dao import CurrencyDao
from model.currency_model import CurrencyModel


class CurrencyController:
    """Обработка запросов по пути '/currency/'"""

    @staticmethod
    def handle_get(handler: BaseHTTPRequestHandler):
        try:
            currency_code = handler.path.split('/')[-1]
            currency_model = CurrencyModel(code=currency_code)
            response = CurrencyDao(currency_model).get_currency()
            BaseController.send_response(handler, response.to_dict(), 200)
        except Exception as error:
            BaseController.error_handler(handler, error)
