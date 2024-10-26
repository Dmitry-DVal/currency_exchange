import json
from http.server import BaseHTTPRequestHandler

import my_exceptions


class BaseController:

    @staticmethod
    def send_response(handler: BaseHTTPRequestHandler, message, code):
        json_response = json.dumps(message, indent=4)
        handler.send_response(code)
        handler.send_header("Access-Control-Allow-Origin", "*")  #
        handler.send_header("Access-Control-Allow-Methods", "GET, POST, PATCH, OPTIONS")  #
        handler.send_header("Access-Control-Allow-Headers", "Content-Type")  #
        handler.send_header("Content-Type", "application/json; charset=UTF-8")
        handler.end_headers()
        handler.wfile.write(json_response.encode("utf-8"))

    @staticmethod
    def error_handler(handler: BaseHTTPRequestHandler, exception: Exception):
        """Централизованная обработка ошибок"""
        if isinstance(exception, my_exceptions.CurrencyCodeError):
            error_message = 'Currency code is not unique or does not match the format'
            BaseController.send_response(handler, {'message': error_message}, 409)
        elif isinstance(exception, my_exceptions.DatabaseUnavailableError):
            error_message = 'Database unavailable'
            BaseController.send_response(handler, {'message': error_message}, 500)
        elif isinstance(exception, my_exceptions.CurrencyNotFoundError):
            error_message = 'Currency not found'
            BaseController.send_response(handler, {'message': error_message}, 404)
        elif isinstance(exception, my_exceptions.ExchangeRateNotFoundError):
            error_message = 'Exchange rate not found'
            BaseController.send_response(handler, {'message': error_message}, 404)
        else:
            error_message = f'Error: {str(exception)}'
            BaseController.send_response(handler, {'message': error_message}, 400)
