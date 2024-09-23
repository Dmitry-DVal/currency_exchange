import sqlite3
import os


class CurrencyRepository:
    """Класс обращается к БД и получает список конкретной валюты"""

    def __init__(self, currency_code):
        self.currency_code = currency_code
        # Построение пути к базе данных относительно текущего файла
        self.db_path = os.path.join(os.path.dirname(__file__), 'dataBase/currencies.db')

    def get_currency(self):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()

            cur.execute("SELECT ID, Fullname, Code, Sign FROM currencies WHERE Code = ?", (self.currency_code,))
            result = cur.fetchall()
            return result

    def currency_exists(self):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM currencies WHERE Code = ?", (self.currency_code,))
            result = cur.fetchall()
            return bool(result)  # Если список не пустой вернет True

    def add_currency(self, request_dict):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO currencies (Code, Fullname, Sign) VALUES (?, ?, ?)",
                        (request_dict['code'], request_dict['name'], request_dict['sign']))
            con.commit()  # Сохраняем изменения в базе данных


if __name__ == '__main__':
    pass
