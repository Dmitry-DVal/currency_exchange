import os
from myExceptions import *
from model.currencyModel import CurrencyModel


class CurrencyDao:
    """Класс обращается к БД и получает список конкретной валюты, добавляет валюту в БД."""

    def __init__(self, currency_model=None):
        self.currency_model = currency_model
        # Построение пути к базе данных относительно текущего файла
        self.db_path = os.path.join(os.path.dirname(__file__), 'dataBase/currencies.db')

    def get_currency(self):
        """Получает информацию по конкретной валюте из БД."""
        query = "SELECT ID, Fullname, Code, Sign FROM currencies WHERE Code = ?"
        result = self._execute_query(query, (self.currency_model.code,))
        currency_model_response = self.make_model_response(result)
        return currency_model_response

    def add_currency(self):
        """Добавляет валюту в БД"""
        query = "INSERT INTO currencies (Code, Fullname, Sign) VALUES (?, ?, ?)"
        self._execute_query(query, (self.currency_model.code, self.currency_model.name, self.currency_model.sign))
        query = "SELECT ID, Fullname, Code, Sign FROM currencies WHERE Code = ?"
        result = self._execute_query(query, (self.currency_model.code,))
        self.currency_model.id = result[0][0]  # Сохраняем ID в модель
        return self.currency_model

    def get_currencies(self) -> list:
        """Получает всю информацию из таблицы currencies"""
        query = "SELECT * FROM currencies"
        return self._execute_query(query)

    def make_model_response(self, data):
        if data:
            self.currency_model = CurrencyModel(data[0][0], data[0][1], data[0][2], data[0][3])
            return self.currency_model
        else:
            raise CurrencyNotFoundError

    def _execute_query(self, query, params=()):
        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor()
                if params:
                    cur.execute(query, params)
                else:
                    cur.execute(query)
                return cur.fetchall()
        except sqlite3.IntegrityError:
            raise CurrencyCodeError("Currency code is not unique or does not match the format")
        except sqlite3.OperationalError:
            raise DatabaseUnavailableError("Database unavailable")
