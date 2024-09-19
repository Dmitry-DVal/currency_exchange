from http import HTTPStatus
from model.currenciesRepository import CureenciesRepository
from model.currencyRepository import CurrencyRepository
from view.jsonFormater import JsonFormater


class GetHandler():

    @staticmethod
    def get_currencies(handler):
        currencies = CureenciesRepository().get_cureencies()
        json_response = JsonFormater().to_json(currencies)
        handler.send_response(HTTPStatus.OK)  # Заголовок. Отправляем статут клиенту
        handler.send_header("Content-Type", 'text/json; charset=UTF-8')  # Передаем заголовок.
        handler.end_headers()

        handler.wfile.write(json_response.encode("utf-8"))


    @staticmethod
    def get_currency(handler, currency_code):
        '''Отправляет результат запроса конкретной валюты.'''
        currency = CurrencyRepository(currency_code).get_cureency()
        if not currency:
            # Если валюта не найдена, отправляем 404 ошибку
            GetHandler.is_not_currency_code(handler)
        else:
            # Если валюта найдена, возвращаем её в формате JSON
            GetHandler.is_currency_code(handler, currency)


    @staticmethod
    def is_currency_code(handler, currency):
        json_response = JsonFormater().to_json(currency)
        handler.send_response(HTTPStatus.OK)
        handler.send_header("Content-Type", "application/json; charset=UTF-8")
        handler.end_headers()

        handler.wfile.write(json_response.encode("utf-8"))

    @staticmethod
    def is_not_currency_code(handler):
        handler.send_response(HTTPStatus.NOT_FOUND)
        handler.send_header("Content-Type", "application/json; charset=UTF-8")
        handler.end_headers()

        error_response = JsonFormater().to_json({"error": "Currency not found"})
        handler.wfile.write(error_response.encode("utf-8"))