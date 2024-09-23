from http import HTTPStatus
from model.currencyRepository import CurrencyRepository
from view.jsonFormater import JsonFormater


class PostHandler():
    """Обработчик POST запросов"""

    @staticmethod
    def add_currency(handler, data):
        request_dict = PostHandler.covert_to_dict(data)
        if not PostHandler.check_fields(request_dict):
            PostHandler.bad_request(handler)
            return
        if CurrencyRepository(request_dict['code']).currency_exists():
            PostHandler.currency_already_exists(handler)
            return
        else:
            PostHandler.add_currency_to_DB(handler, request_dict)

    @staticmethod
    def covert_to_dict(data):
        'Формотирует полученный запрос в словарь'
        result = {}
        for i in data.split('&'):
            result[i.split('=')[0]] = i.split('=')[1]
        return result

    @staticmethod
    def check_fields(your_dict):
        'Проверяет что все необходимые поля присутствуют в запросе'
        response = []
        for i in ['name', 'code', 'sign']:
            response.append(i in your_dict)
        return all(response)

    @staticmethod
    def bad_request(handler):
        handler.send_response(HTTPStatus.BAD_REQUEST)  # 400
        handler.send_header("Content-Type", "text/html; charset=UTF-8")
        handler.end_headers()
        handler.wfile.write("<h1>400 Required form field is missing/h1>".encode("utf-8"))

    @staticmethod
    def currency_already_exists(handler):
        handler.send_response(HTTPStatus.CONFLICT)  # 409
        handler.send_header("Content-Type", "text/html; charset=UTF-8")
        handler.end_headers()
        handler.wfile.write("<h1>409 Currency with this code already exists/h1>".encode("utf-8"))

    @staticmethod
    def add_currency_to_DB(handler, request_dict):
        CurrencyRepository(request_dict['code']).add_currency(request_dict)
        currency = CurrencyRepository(request_dict['code']).get_currency()
        json_response = JsonFormater().to_json(currency)
        handler.send_response(HTTPStatus.OK)  # 200
        handler.send_header("Content-Type", "application/json; charset=UTF-8")
        handler.end_headers()

        handler.wfile.write(json_response.encode("utf-8"))
