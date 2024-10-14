from http.server import BaseHTTPRequestHandler
from http import HTTPStatus
from controller.jsonFormater import JsonFormater


class Response:
    """Обработчик ответов"""

    @staticmethod
    def good_request_200(handler: BaseHTTPRequestHandler, currency: list):
        json_response = JsonFormater().to_json(currency)
        Response.send_json_response(handler, json_response, HTTPStatus.OK)

    @staticmethod
    def currency_code_exists(handler: BaseHTTPRequestHandler, message: str = "CurrencyCodeExistsError"):
        error_response = JsonFormater().to_json({"error": message})
        Response.send_json_response(handler, error_response, HTTPStatus.CONFLICT)

    @staticmethod
    def send_json_response(handler: BaseHTTPRequestHandler, json_response, status_code):
        handler.send_response(status_code)
        handler.send_header("Content-Type", "application/json; charset=UTF-8")
        handler.end_headers()
        handler.wfile.write(json_response.encode("utf-8"))
    #
    @staticmethod
    def send_error(handler, message, status_code):
        handler.send_json_response(handler, {"error": message}, status_code)
