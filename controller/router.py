from http.server import BaseHTTPRequestHandler
from controller.currenciesController import CurrenciesController


class Router(BaseHTTPRequestHandler):
    """Распределяет запросы по нужным контроллерам, выдает ошибку если такой страницы не существует"""

    def do_POST(self):
        """Обработчик POST запросов"""
        if self.path.startswith("/currencies"):
            CurrenciesController.handle_post(self)
        else:
            self.send_page_not_found()

    def send_page_not_found(self):
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"404 Not Found")