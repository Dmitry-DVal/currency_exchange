import sqlite3
import os


class CurrenciesRepository:
    """Класс обращается к БД и получить список всех валют"""

    def get_cureencies(self) -> list:
        # Построение пути к базе данных относительно текущего файла
        db_path = os.path.join(os.path.dirname(__file__), 'dataBase/currencies.db')
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()

            cur.execute("SELECT * FROM currencies")
            result = cur.fetchall()
            return result


if __name__ == '__main__':
    print(CureenciesRepository().get_cureencies())
