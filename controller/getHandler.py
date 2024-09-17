from http import HTTPStatus
from controller.ourHandler import OurHandler


class GetHandler(OurHandler):
    def __init__(self, path):
        self.path = path

    def do_GET(self):
        self.get_currencies()

    def get_currencies(self):
        self.send_response(HTTPStatus.OK)  # Заголовок. Отправляем статут клиенту
        self.send_header("Content-Type", 'text/html; charset=UTF-8')  # Передаем заголовок.
        self.end_headers()

        self.wfile.write("<h1>Здесь будет весь список валют</h1>".encode("utf-8"))  # Запись ответа клиенту
