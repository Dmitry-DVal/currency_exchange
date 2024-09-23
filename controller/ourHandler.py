from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
from controller.getHandler import GetHandler
from controller.postHandler import PostHandler


class OurHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/currencies':
            GetHandler.get_currencies(self)
        elif self.path.startswith('/currency/'):
            # Извлечение кода валюты из пути
            currency_code = self.path.split('/')[-1]
            GetHandler.get_currency(self, currency_code)
        else:
            self.page_not_found()

# корректный запрос
# curl -X POST http://localhost:8000/currencies -d "name=Albanian Lek&code=ALL&sign=L" -H "Content-Type: application/x-www-form-urlencoded"
# не хватает поля
# curl -X POST http://localhost:8000/currencies -d "code=ALL&sign=L" -H "Content-Type: application/x-www-form-urlencoded"
# уже есть такой код валюты
# curl -X POST http://localhost:8000/currencies -d "name=Albanian Lek&code=RUB&sign=L" -H "Content-Type: application/x-www-form-urlencoded"

    def do_POST(self):
        if self.path == '/currencies':
            content_length = int(self.headers['Content-Length'])  # Получаем длину содержимого
            post_data = self.rfile.read(content_length).decode('utf-8')  # Читаем и декодируем данные
            # print("POST data:", post_data)  # Выводим данные, чтобы понять как они выглядят
            PostHandler.add_currency(self, post_data)
        else:
            self.page_not_found()

    def page_not_found(self):
        self.send_response(HTTPStatus.NOT_FOUND)
        self.send_header("Content-Type", "text/html; charset=UTF-8")  # Передаем заголовок.
        self.end_headers()  # Закрываем заголовок

        self.wfile.write("<h1>404 NOT FOUND!</h1>".encode("utf-8"))  # Запись ответа клиенту


if __name__ == '__main__':
    pass
