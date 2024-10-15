import sqlite3
import os
from myExceptions import *


class CurrencyDao:
    """Класс обращается к БД и получает список конкретной валюты, добавляет валюту в БД."""

    def __init__(self, currency_model=None):
        self.currency_model = currency_model
        # Построение пути к базе данных относительно текущего файла
        self.db_path = os.path.join(os.path.dirname(__file__), 'dataBase/currencies.db')

    def get_currency(self):
        """Получает информацию по конкретной валюте из БД."""
        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor()
                cur.execute("SELECT ID, Fullname, Code, Sign FROM currencies WHERE Code = ?",
                            (self.currency_model.code,))
                result = cur.fetchall()
                self.currency_model.id = result[0][0]
                return self.currency_model
        except sqlite3.OperationalError:
            raise DatabaseUnavailableError("Database unavailable")

    def add_currency(self):
        """Добавляет валюту в БД"""
        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO currencies (Code, Fullname, Sign) VALUES (?, ?, ?)",
                            (self.currency_model.code, self.currency_model.name, self.currency_model.sign))
                con.commit()  # Сохраняем изменения в базе данных
            self.get_currency()
        except sqlite3.IntegrityError:
            raise CurrencyCodeError("Currency code is not unique or does not match the format")
        except sqlite3.OperationalError:
            raise DatabaseUnavailableError("Database unavailable")

    def get_currencies(self) -> list:
        """Получает всю информацию из таблицы currencies"""
        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor()

                cur.execute("SELECT * FROM currencies")
                result = cur.fetchall()
                return result
        except sqlite3.OperationalError:
            raise DatabaseUnavailableError("Database unavailable")
