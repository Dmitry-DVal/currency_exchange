from http.server import BaseHTTPRequestHandler
from service.currenciesService import CurrenciesService
from controller.baseController import BaseController


class CurrencyController(BaseController):
    """Обработка запросов по пути '/currency/'"""

    @staticmethod
    def handle_get(handler: BaseHTTPRequestHandler):
        try:
            currency_code = handler.path.split('/')[-1]
            response = CurrenciesService.get_currency(currency_code)
            BaseController.send_response(handler, response, 200)
        except Exception as e:
            BaseController.error_handler(handler, e)
