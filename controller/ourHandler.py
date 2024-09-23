from http.server import BaseHTTPRequestHandler
from controller.getHandler import GetHandler
from controller.postHandler import PostHandler
from controller.responseHandler import ResponseHandler


class OurHandler(BaseHTTPRequestHandler):
    """Главный обработчик запросов, распределяет запросы, выдает ошибку если такой страницы не существует"""

    def do_GET(self):
        if self.path == '/currencies':
            GetHandler.get_currencies(self)
        elif self.path.startswith('/currency/'):
            # Извлечение кода валюты из пути
            currency_code = self.path.split('/')[-1]
            GetHandler.get_currency(self, currency_code)
        else:
            ResponseHandler.page_not_found_400(self)

    def do_POST(self):
        if self.path == '/currencies':
            content_length = int(self.headers['Content-Length'])  # Получаем длину содержимого
            post_data = self.rfile.read(content_length).decode('utf-8')  # Читаем и декодируем данные
            PostHandler.add_currency(self, post_data)
        else:
            ResponseHandler.page_not_found_400(self)


if __name__ == '__main__':
    pass
