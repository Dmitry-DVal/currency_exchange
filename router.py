from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

from controller import CurrencyController, CurrenciesController, ExchangeRateController, ExchangeRatesController, \
    ExchangeController

routes = {
    'POST': {
        'currencies': CurrenciesController.handle_post,
        'exchangeRates': ExchangeRatesController.handle_post,
    },
    'GET': {
        'currencies': CurrenciesController.handle_get,
        'currency': CurrencyController.handle_get,
        'exchangeRate': ExchangeRateController.handle_get,
        'exchangeRates': ExchangeRatesController.handle_get,
        'exchange': ExchangeController.handle_get
    },
    'PATCH': {
        'exchangeRate': ExchangeRateController.handle_patch,
    }
}


class Router(BaseHTTPRequestHandler):
    """Распределяет запросы по нужным контроллерам, выдает ошибку если такой страницы не существует"""

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PATCH, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        """Обработчик POST запросов"""
        handler = self.select_handler('POST')
        self.start_handling(handler)

    def do_GET(self):
        """Обработчик GET запросов"""
        handler = self.select_handler('GET')
        self.start_handling(handler)

    def do_PATCH(self):
        """Обработчик PATCH запросов"""
        handler = self.select_handler('PATCH')
        self.start_handling(handler)

    def start_handling(self, handler):
        if handler:
            handler(self)
        else:
            self.send_page_not_found()

    def select_handler(self, type_http_request):
        parsed_path = urlparse(self.path)
        path = parsed_path.path.split('/')[1]
        handler = routes[type_http_request].get(path)
        return handler

    def send_page_not_found(self):
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"404 Not Found")
