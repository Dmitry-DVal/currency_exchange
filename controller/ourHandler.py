from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
from view.jsonFormater import JsonFormater
from model.currenciesRepository import CureenciesRepository


class OurHandler(BaseHTTPRequestHandler):
    pass

    def do_GET(self):
        if self.path == '/currencies':
            self.get_currencies()

    def get_currencies(self):
        currencies = CureenciesRepository().get_cureencies()
        json_response = JsonFormater().to_json(currencies)
        self.send_response(HTTPStatus.OK)  # Заголовок. Отправляем статут клиенту
        self.send_header("Content-Type", 'text/json; charset=UTF-8')  # Передаем заголовок.
        self.end_headers()

        self.wfile.write(json_response.encode("utf-8"))


if __name__ == '__main__':
    pass
