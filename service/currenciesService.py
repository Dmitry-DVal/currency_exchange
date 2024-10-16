from model.currencyModel import CurrencyModel
from dao.currencyDao import CurrencyDao


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
        except Exception as error:
            raise error

    @classmethod
    def get_currencies(cls):
        try:
            result = CurrencyDao().get_currencies()
            currencies = cls.make_currencies_dict(result)
            return currencies
        except Exception as error:
            raise error

    @classmethod
    def get_currency(cls, currency_code):
        currency_model = CurrencyModel(None, currency_code, None)
        try:
            result = CurrencyDao(currency_model).get_currency()
            currency = cls.make_currencies_dict(result)
            return currency
        except Exception as error:
            raise error

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
