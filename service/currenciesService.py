from model.currencyModel import CurrencyModel
from dao.currencyDao import CurrencyDao
from myExceptions import *

class CurrenciesService:
    def __init__(self, dto):
        self.dto = dto

    def make_model(self):
        return CurrencyModel(self.dto.name, self.dto.code, self.dto.sign)  # currencyModel

    def add_currency_to_db(self):  # currencyDao
        currency_model = self.make_model()
        try:
            CurrencyDao(currency_model).add_currency()
            return currency_model.__dict__
        except CurrencyCodeError as e:
            # Можно просто прокинуть исключение дальше или вернуть его в контроллер в нужном формате
            return {'error': str(e), 'error_code': 409}
        except DatabaseUnavailableError as e:
            return {'error': str(e), 'error_code': 500}

    @classmethod
    def get_currencies(cls):
        try:
            result = CurrencyDao().get_currencies()
            currencies = cls.make_currencies_dict(result)
            return currencies
        except DatabaseUnavailableError as e:
            return {'error': str(e), 'error_code': 500}

    @staticmethod
    def make_currencies_dict(data: list) -> list:
        result = []
        for row in data:
            result.append({
                "id": row[0],
                "code": row[1],
                "name": row[2],
                "sign": row[3]
            })
        return result
