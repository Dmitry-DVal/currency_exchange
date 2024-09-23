from http import HTTPStatus
from view.jsonFormater import JsonFormater


class ResponseHandler:

    @staticmethod
    def good_request_200(handler, currency):
        json_response = JsonFormater().to_json(currency)
        handler.send_response(HTTPStatus.OK)  # 200
        handler.send_header("Content-Type", "application/json; charset=UTF-8")
        handler.end_headers()

        handler.wfile.write(json_response.encode("utf-8"))

    @staticmethod
    def bad_request_400(handler):
        handler.send_response(HTTPStatus.BAD_REQUEST)  # 400
        handler.send_header("Content-Type", "text/html; charset=UTF-8")
        handler.end_headers()
        handler.wfile.write("<h1>400 Required form field is missing/h1>".encode("utf-8"))

    @staticmethod
    def page_not_found_400(handler):
        handler.send_response(HTTPStatus.NOT_FOUND)
        handler.send_header("Content-Type", "text/html; charset=UTF-8")  # Передаем заголовок.
        handler.end_headers()  # Закрываем заголовок

        handler.wfile.write("<h1>404 NOT FOUND!</h1>".encode("utf-8"))  # Запись ответа клиенту

    @staticmethod
    def currency_not_found(handler):
        handler.send_response(HTTPStatus.NOT_FOUND)  # 404
        handler.send_header("Content-Type", "application/json; charset=UTF-8")
        handler.end_headers()

        error_response = JsonFormater().to_json({"error": "Currency not found"})
        handler.wfile.write(error_response.encode("utf-8"))

    @staticmethod
    def currency_already_exists_409(handler):
        handler.send_response(HTTPStatus.CONFLICT)  # 409
        handler.send_header("Content-Type", "text/html; charset=UTF-8")
        handler.end_headers()
        handler.wfile.write("<h1>409 Currency with this code already exists/h1>".encode("utf-8"))