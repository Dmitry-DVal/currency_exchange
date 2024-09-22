from http import HTTPStatus
from view.jsonFormater import JsonFormater

class PostHandler():

    @staticmethod
    def add_currency(handler, data):
        print("Received data:", data, type(data))  # Проверка, Выводим данные, полученные из POST-запроса (сейчас это json)
        result = PostHandler.covert_to_dict(data)
        print(result, type(result)) # Проверка, преобразования в словарь dict
        #print(PostHandler.check_fields(result))
        handler.send_response(HTTPStatus.OK)
        handler.send_header("Content-Type", "text/html; charset=UTF-8")
        handler.end_headers()
        handler.wfile.write("<h1>200 We'll add your currency</h1>".encode("utf-8"))
        result = {}
        for pair in data.split():
            key, value = 1, 1


    @staticmethod
    def covert_to_dict(data):
        result = {}
        for i in data.split('&'):
            result[i.split('=')[0]] = i.split('=')[1]
        return result

    # @staticmethod
    # def check_fields(your_dict):
    #     return all(your_dict[h] in your_dict for ['name', 'code', 'sign'])

    def currency_already_exists():
        pass




# Получили данные
# Проверили что данных достатоно и они корретны (если нет отправили ошибку) (400 нет нужного поля или формат не верный,  409 ваолюта с этим кодом существует уже, 200 ок)
# Данные корректны - внесли в таблице
# Отправили результат в формате джсон, результат вставленная валюта в таблицу