from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
from controller.getHandler import GetHandler



class OurHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/currencies':
            GetHandler.get_currencies(self)
        elif self.path.startswith('/currency/'):
            #Извлечение кода валюты из пути
            currency_code = self.path.split('/')[-1]
            GetHandler.get_currency(self, currency_code)
        else:
            self.page_not_found()

    def page_not_found(self):
        self.send_response(HTTPStatus.NOT_FOUND)
        self.send_header("Content-Type", "text/html; charset=UTF-8")  # Передаем заголовок.
        self.end_headers()  # Закрываем заголовок

        self.wfile.write("<h1>404 NOT FOUND!</h1>".encode("utf-8"))  # Запись ответа клиенту


if __name__ == '__main__':
    pass
