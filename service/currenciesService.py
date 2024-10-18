from model.currencyModel import CurrencyModel
from dao.currencyDao import CurrencyDao


class CurrenciesService:
    def __init__(self, dto=None):
        self.dto = dto

    def make_model(self):
        return CurrencyModel(name=self.dto.name, code=self.dto.code, sign=self.dto.sign)  # currencyModel

    def get_currencies(self) -> dict or Exception:
        try:
            result = CurrencyDao().get_currencies()
            currencies = self.make_currencies_dict(result)
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
