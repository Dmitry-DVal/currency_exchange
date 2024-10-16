from http.server import BaseHTTPRequestHandler
import json
from myExceptions import *


class BaseController:
    @staticmethod
    def send_response(handler: BaseHTTPRequestHandler, data: dict, status_code: int):
        json_response = json.dumps(data, indent=4)
        handler.send_response(status_code)
        handler.send_header("Content-Type", "application/json; charset=UTF-8")
        handler.end_headers()
        handler.wfile.write(json_response.encode("utf-8"))

    @staticmethod
    def error_handler(handler: BaseHTTPRequestHandler, exception: Exception):
        """Централизованная обработка ошибок"""
        if isinstance(exception, CurrencyCodeError):
            error_message = 'Currency code is not unique or does not match the format'
            BaseController.send_response(handler, {'message': error_message}, 409)
        elif isinstance(exception, DatabaseUnavailableError):
            error_message = 'Database unavailable'
            BaseController.send_response(handler, {'message': error_message}, 500)
        else:
            error_message = f'Error: {str(exception)}'
            BaseController.send_response(handler, {'message': error_message}, 400)
