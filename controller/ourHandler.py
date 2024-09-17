from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
from view.jsonFormater import JsonFormater
from model.currenciesRepository import CureenciesRepository
from model.currencyRepository import CurrencyRepository



class OurHandler(BaseHTTPRequestHandler):
    pass

    def do_GET(self):
        if self.path == '/currencies':
            self.get_currencies()
        elif self.path.startswith('/currency/'):
            #Извлечение кода валюты из пути
            currency_code = self.path.split('/')[-1]
            self.get_currency(currency_code)
        else:
            self.page_not_found()

    def get_currencies(self):
        currencies = CureenciesRepository().get_cureencies()
        json_response = JsonFormater().to_json(currencies)
        self.send_response(HTTPStatus.OK)  # Заголовок. Отправляем статут клиенту
        self.send_header("Content-Type", 'text/json; charset=UTF-8')  # Передаем заголовок.
        self.end_headers()

        self.wfile.write(json_response.encode("utf-8"))

    def get_currency(self, currency_code):
        '''Отправляет результат запроса конкретной валюты.'''
        currency = CurrencyRepository(currency_code).get_cureency()
        if not currency:
            # Если валюта не найдена, отправляем 404 ошибку
            self.is_not_currency_code()
        else:
            # Если валюта найдена, возвращаем её в формате JSON
            self.is_currency_code(currency)


    def is_currency_code(self, currency):
        json_response = JsonFormater().to_json(currency)
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json; charset=UTF-8")
        self.end_headers()

        self.wfile.write(json_response.encode("utf-8"))

    def is_not_currency_code(self):
        self.send_response(HTTPStatus.NOT_FOUND)
        self.send_header("Content-Type", "application/json; charset=UTF-8")
        self.end_headers()

        error_response = JsonFormater().to_json({"error": "Currency not found"})
        self.wfile.write(error_response.encode("utf-8"))

    def page_not_found(self):
        self.send_response(HTTPStatus.NOT_FOUND)
        self.send_header("Content-Type", "text/html; charset=UTF-8")  # Передаем заголовок.
        self.end_headers()  # Закрываем заголовок

        self.wfile.write("<h1>404 NOT FOUND!</h1>".encode("utf-8"))  # Запись ответа клиенту


if __name__ == '__main__':
    pass
