from http.server import BaseHTTPRequestHandler
from controller.jsonFormater import JsonFormater


class Response:
    """Обработчик ответов"""

    @staticmethod
    def send_response(handler: BaseHTTPRequestHandler, data: list, status_code: int):
        json_response = JsonFormater().to_json(data)
        handler.send_response(status_code)
        handler.send_header("Content-Type", "application/json; charset=UTF-8")
        handler.end_headers()
        handler.wfile.write(json_response.encode("utf-8"))
