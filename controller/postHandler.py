from model.currencyRepository import CurrencyRepository
from controller.responseHandler import ResponseHandler


class PostHandler:
    """Обработчик POST запросов"""

    @staticmethod
    def add_currency(handler, data):
        request_dict = PostHandler.covert_to_dict(data)
        if not PostHandler.check_fields(request_dict):
            ResponseHandler.bad_request_400(handler)
            return
        if CurrencyRepository(request_dict['code']).currency_exists():
            ResponseHandler.currency_already_exists_409(handler)
            return
        else:
            PostHandler.add_currency_to_db(handler, request_dict)

    @staticmethod
    def covert_to_dict(data):
        """Форматирует полученный запрос в словарь"""
        result = {}
        for i in data.split('&'):
            result[i.split('=')[0]] = i.split('=')[1]
        return result

    @staticmethod
    def check_fields(your_dict):
        """Проверяет что все необходимые поля присутствуют в запросе"""
        response = []
        for i in ['name', 'code', 'sign']:
            response.append(i in your_dict)
        return all(response)

    @staticmethod
    def add_currency_to_db(handler, request_dict):
        CurrencyRepository(request_dict['code']).add_currency(request_dict)
        currency = CurrencyRepository(request_dict['code']).get_currency()
        ResponseHandler.good_request_200(handler, currency)
