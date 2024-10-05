from http.server import BaseHTTPRequestHandler
from http import HTTPStatus
from view.jsonFormater import JsonFormater


class ResponseHandler:
    """Обработчик ошибок"""

    @staticmethod
    def good_request_200(handler: BaseHTTPRequestHandler, currency: list):
        json_response = JsonFormater().to_json(currency)
        ResponseHandler.send_json_response(handler, json_response, HTTPStatus.OK)

    @staticmethod
    def good_transfer_currency_request_200(handler: BaseHTTPRequestHandler, exchange_rate: list, amount: float,
                                           rate: float):
        json_response = JsonFormater().transfer_currency_to_json(exchange_rate, amount, rate)
        ResponseHandler.send_json_response(handler, json_response, HTTPStatus.OK)

    @staticmethod
    def bad_request_400(handler: BaseHTTPRequestHandler, message: str = 'Required form field is missing'):
        error_response = JsonFormater().to_json({"error": message})
        ResponseHandler.send_json_response(handler, error_response, HTTPStatus.BAD_REQUEST)

    @staticmethod
    def page_not_found_400(handler: BaseHTTPRequestHandler):
        handler.send_response(HTTPStatus.NOT_FOUND)
        handler.send_header("Content-Type", "text/html; charset=UTF-8")  # Передаем заголовок.
        handler.end_headers()  # Закрываем заголовок

        handler.wfile.write("<h1>404 NOT FOUND!</h1>".encode("utf-8"))  # Запись ответа клиенту

    @staticmethod
    def currency_not_found(handler: BaseHTTPRequestHandler, message: str = "Currency not found"):
        error_response = JsonFormater().to_json({"error": message})
        ResponseHandler.send_json_response(handler, error_response, HTTPStatus.NOT_FOUND)

    @staticmethod
    def already_exists_409(handler: BaseHTTPRequestHandler, message: str = "Currency with this code already exists"):
        error_response = JsonFormater().to_json({"error": message})
        ResponseHandler.send_json_response(handler, error_response, HTTPStatus.CONFLICT)

    @staticmethod
    def server_error_500(handler: BaseHTTPRequestHandler,
                         message: str = "500 Server-side error. The database is unavailable"):
        error_response = JsonFormater().to_json({"error": message})
        ResponseHandler.send_json_response(handler, error_response, HTTPStatus.INTERNAL_SERVER_ERROR)

    @staticmethod
    def send_json_response(handler: BaseHTTPRequestHandler, json_response, status_code):
        handler.send_response(status_code)
        handler.send_header("Content-Type", "application/json; charset=UTF-8")
        handler.end_headers()
        handler.wfile.write(json_response.encode("utf-8"))

    @staticmethod
    def send_error(handler, message, status_code):
        handler.send_json_response(handler, {"error": message}, status_code)
