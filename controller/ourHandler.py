import sqlite3
from http.server import BaseHTTPRequestHandler
from controller.getHandler import GetHandler
from controller.postHandler import PostHandler
from controller.responseHandler import ResponseHandler


# Код с обработкой исключений повторяется, можно отлавливать исключение при попытке подключения к БД

class OurHandler(BaseHTTPRequestHandler):
    """Главный обработчик запросов, распределяет запросы, выдает ошибку если такой страницы не существует"""

    def do_GET(self):
        if self.path == '/currencies':
            try:
                GetHandler.get_currencies(self)
            except sqlite3.OperationalError:
                ResponseHandler.server_error_500(self)
        elif self.path.startswith('/currency/'):
            # Извлечение кода валюты из пути
            currency_code = self.path.split('/')[-1]
            try:
                GetHandler.get_currency(self, currency_code)
            except sqlite3.OperationalError:
                ResponseHandler.server_error_500(self)
        elif self.path == '/exchangeRates':
            try:
                GetHandler.get_exchange_rates(self)
            except sqlite3.OperationalError:
                ResponseHandler.server_error_500(self)
        elif self.path.startswith('/exchangeRate'):
            base_currency_code, target_currency_code = self.path.split('/')[-1][:3], self.path.split('/')[-1][3:]
            print(base_currency_code, target_currency_code)
            try:
                GetHandler.get_exchange_rate(self, base_currency_code, target_currency_code)
            except sqlite3.OperationalError:
                ResponseHandler.server_error_500(self)
        else:
            ResponseHandler.page_not_found_400(self)

    def do_POST(self):
        if self.path == '/currencies':
            content_length = int(self.headers['Content-Length'])  # Получаем длину содержимого
            post_data = self.rfile.read(content_length).decode('utf-8')  # Читаем и декодируем данные
            try:
                PostHandler.add_currency(self, post_data)
            except sqlite3.OperationalError:
                ResponseHandler.server_error_500(self)
        else:
            ResponseHandler.page_not_found_400(self)


if __name__ == '__main__':
    pass
