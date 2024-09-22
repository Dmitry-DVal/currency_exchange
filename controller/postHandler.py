from http import HTTPStatus
from model.currencyRepository import CurrencyRepository
from view.jsonFormater import JsonFormater


class PostHandler():

    @staticmethod
    def add_currency(handler, data):
        print("Received data:", data,
              type(data))  # Проверка, Выводим данные, полученные из POST-запроса (сейчас это json)
        request_dict = PostHandler.covert_to_dict(data)
        print(request_dict, type(request_dict))  # Проверка, преобразования в словарь dict
        print("Присутсвие нужных полей =", PostHandler.check_fields(request_dict))  # Проверка, что нужные поля есть
        if not PostHandler.check_fields(request_dict):
            PostHandler.bad_request(handler)
        if CurrencyRepository(request_dict['code']).currency_exists():
            print("Валюта уже есть в БД")
            PostHandler.currency_already_exists(handler)
        else:
            pass
            # Добавить в БД
            # Вывести результат
        # handler.send_response(HTTPStatus.OK)
        # handler.send_header("Content-Type", "text/html; charset=UTF-8")
        # handler.end_headers()
        # handler.wfile.write("<h1>200 We'll add your currency</h1>".encode("utf-8"))


    @staticmethod
    def covert_to_dict(data):
        result = {}
        for i in data.split('&'):
            result[i.split('=')[0]] = i.split('=')[1]
        return result

    @staticmethod
    def check_fields(your_dict):
        response = []
        for i in ['name', 'code', 'sign']:
            response.append(i in your_dict)
        return all(response)

    @staticmethod
    def bad_request(handler):
        handler.send_response(HTTPStatus.BAD_REQUEST)
        handler.send_header("Content-Type", "text/html; charset=UTF-8")
        handler.end_headers()
        handler.wfile.write("<h1>400 Required form field is missing/h1>".encode("utf-8"))


    @staticmethod
    def currency_already_exists(handler):
        handler.send_response(HTTPStatus.CONFLICT)
        handler.send_header("Content-Type", "text/html; charset=UTF-8")
        handler.end_headers()
        handler.wfile.write("<h1>409 Currency with this code already exists/h1>".encode("utf-8"))

# Получили данные
# Проверили что данных достатоно и они корретны (если нет отправили ошибку) (400 нет нужного поля или формат не верный,  409 ваолюта с этим кодом существует уже, 200 ок)
# Данные корректны - внесли в таблице
# Отправили результат в формате джсон, результат вставленная валюта в таблицу
