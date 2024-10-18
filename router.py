from http.server import BaseHTTPRequestHandler
from controller.currenciesController import CurrenciesController
from controller.currencyController import CurrencyController
from controller.exchangeRateController import ExchangeRateController

routes = {
    'POST': {
        'currencies': CurrenciesController.handle_post,
        # 'exchangeRates': ExchangeRateController.handle_post,
        # '/currency': CurrencyController.handle_post,
        # '/exchangeRates': ExchangeRatesController.handle_post,
        # '/exchange': ExchangeCurrencyController.handle_post
    },
    'GET': {
        'currencies': CurrenciesController.handle_get,
        'currency': CurrencyController.handle_get,
        'exchangeRate': ExchangeRateController.handle_get,
        # '/exchangeRates': ExchangeRatesController.handle_get,
        # '/exchangeRate': ExchangeRateController.handle_get,
        # '/exchange': ExchangeCurrencyController.handle_get
    },
    'PATCH': {
        'exchangeRate': ExchangeRateController.handle_patch,
    }
}


class Router(BaseHTTPRequestHandler):
    """Распределяет запросы по нужным контроллерам, выдает ошибку если такой страницы не существует"""

    def do_POST(self):
        """Обработчик POST запросов"""
        path = self.path.split('/')[1]
        handler = routes['POST'].get(path)
        if handler:
            handler(self)
        else:
            self.send_page_not_found()

    def do_GET(self):
        """Обработчик GET запросов"""
        path = self.path.split('/')[1]
        handler = routes['GET'].get(path)
        if handler:
            handler(self)
        else:
            self.send_page_not_found()

    def do_PATCH(self):
        """Обработчик PATCH запросов"""
        path = self.path.split('/')[1]
        handler = routes['PATCH'].get(path)
        if handler:
            handler(self)
        else:
            self.send_page_not_found()

    def send_page_not_found(self):
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"404 Not Found")
