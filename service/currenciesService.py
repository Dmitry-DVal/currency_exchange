from model.currencyModel import CurrencyModel
from dao.currencyDao import CurrencyDao


class CurrenciesService:
    def __init__(self, dto):
        self.dto = dto

    def make_model(self):
        return CurrencyModel(self.dto.name, self.dto.code, self.dto.sign)  # currencyModel

    def add_currency_to_db(self):  # currencyDao
        currency_model = self.make_model()
        CurrencyDao(currency_model).add_currency()
        return currency_model.__dict__
