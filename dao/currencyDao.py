from model.currencyModel import CurrencyModel
from dao.baseDao import BaseDao
from dao import SQLqueries


class CurrencyDao(BaseDao):
    """Класс обращается к БД и получает список конкретной валюты, добавляет валюту в БД."""

    def __init__(self, currency_model: CurrencyModel = None):
        super().__init__()
        self.currency = currency_model

    def get_currency(self) -> CurrencyModel:
        """Получает информацию по конкретной валюте из БД."""
        query = SQLqueries.get_currency
        result = self._execute_query(query, (self.currency.code,))
        currency_model_response = self.make_currency_model_response(result)
        return currency_model_response

    def add_currency(self):
        """Добавляет валюту в БД"""
        query = SQLqueries.add_currency
        self._execute_query(query, (self.currency.code, self.currency.name, self.currency.sign))
        query = SQLqueries.get_currency
        result = self._execute_query(query, (self.currency.code,))
        currency_model = self.make_currency_model_response(result)
        return currency_model

    def get_currencies(self) -> list:
        """Получает всю информацию из таблицы currencies"""
        query = "SELECT * FROM currencies"
        return self._execute_query(query)
