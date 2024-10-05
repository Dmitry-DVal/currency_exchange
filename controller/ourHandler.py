import sqlite3
from http.server import BaseHTTPRequestHandler
from controller.getHandler import GetHandler
from controller.postHandler import PostHandler
from controller.responseHandler import ResponseHandler
from controller.patchHandler import PatchHandler


class OurHandler(BaseHTTPRequestHandler):
    """Главный обработчик запросов, распределяет запросы, выдает ошибку если такой страницы не существует"""

    def handle_db_errors(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except sqlite3.OperationalError:
                ResponseHandler.server_error_500(args[0])  # передаем handler
        return wrapper

    @handle_db_errors
    def do_GET(self):
        """Обработчик GET запросов"""
        if self.path == '/currencies':
            GetHandler.get_currencies(self)
        elif self.path.startswith('/currency/'):
            currency_code = self.path.split('/')[-1]
            GetHandler.get_currency(self, currency_code)
        elif self.path == '/exchangeRates':
            GetHandler.get_exchange_rates(self)
        elif self.path.startswith('/exchangeRate/'):
            base_currency_code, target_currency_code = self.path.split('/')[-1][:3], self.path.split('/')[-1][3:]
            GetHandler.get_exchange_rate(self, base_currency_code, target_currency_code)
        elif self.path.startswith('/exchange?from='):
            GetHandler.get_exchange(self, self.path)
        else:
            ResponseHandler.page_not_found_400(self)

    @handle_db_errors
    def do_POST(self):
        """Обработчик POST запросов"""
        if self.path == '/currencies':
            content_length = int(self.headers['Content-Length'])  # Получаем длину содержимого
            post_data = self.rfile.read(content_length).decode('utf-8')  # Читаем и декодируем данные
            PostHandler.add_currency(self, post_data)
        elif self.path == '/exchangeRates':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            PostHandler.add_exchange_rates(self, post_data)
        else:
            ResponseHandler.page_not_found_400(self)

    @handle_db_errors
    def do_PATCH(self):
        """Обработчик PATCH запросов"""
        if self.path.startswith('/exchangeRate'):
            base_currency_code, target_currency_code = self.path.split('/')[-1][:3], self.path.split('/')[-1][3:]
            content_length = int(self.headers['Content-Length'])
            patch_data = self.rfile.read(content_length).decode('utf-8')
            PatchHandler.patch_exchange_rate(self, base_currency_code, target_currency_code, patch_data)
        else:
            ResponseHandler.page_not_found_400(self)


if __name__ == '__main__':
    pass