import sqlite3
import os


class CurrencyRepository:
    """Класс обращается к БД и получает список конкретной валюты"""

    def __init__(self, currency_code):
        self.currency_code = currency_code

    def get_cureency(self):
        # Построение пути к базе данных относительно текущего файла
        db_path = os.path.join(os.path.dirname(__file__), 'dataBase/currencies.db')
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()

            cur.execute("SELECT ID, Fullname, Code, Sign FROM currencies WHERE Code = ?", (self.currency_code,))
            result = cur.fetchall()
            return result


if __name__ == '__main__':
    pass