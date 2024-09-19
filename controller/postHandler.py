from http import HTTPStatus
from view.jsonFormater import JsonFormater

class PostHandler():

    @staticmethod
    def add_currency(handler, data):
        print("Received data:", data, type(data))  # Выводим данные, полученные из POST-запроса
        handler.send_response(HTTPStatus.OK)
        handler.send_header("Content-Type", "text/html; charset=UTF-8")
        handler.end_headers()
        handler.wfile.write("<h1>200 We'll add your currency</h1>".encode("utf-8"))
        result = {}
        for pair in data.split():
            key, value = 1, 1


    def covert_to_dict(self):
        pass
    def all_fields_exist(self):
        pass
    def currency_already_exists():
        pass




# Получили данные
# Проверили что данных достатоно и они корретны (если нет отправили ошибку) (400 нет нужного поля или формат не верный,  409 ваолюта с этим кодом существует уже, 200 ок)
# Данные корректны - внесли в таблице
# Отправили результат в формате джсон, результат вставленная валюта в таблицу