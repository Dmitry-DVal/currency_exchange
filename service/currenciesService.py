from model.currencyModel import CurrencyModel
from dao.currencyDao import CurrencyDao


class CurrenciesService:
    def __init__(self, dto):
        self.dto = dto

    def make_model(self):
        return CurrencyModel(name=self.dto.name, code=self.dto.code, sign=self.dto.sign)  # currencyModel

    @classmethod
    def get_currencies(cls):
        try:
            result = CurrencyDao().get_currencies()
            currencies = cls.make_currencies_dict(result)
            return currencies
        except Exception as error:
            raise error

    @staticmethod
    def make_currencies_dict(data: list) -> list:
        result = []
        for row in data:
            result.append({
                "id": row[0],
                "name": row[1],
                "code": row[2],
                "sign": row[3]
            })
        return result
