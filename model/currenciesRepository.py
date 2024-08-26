import sqlite3
import os


class CureenciesRepository:
    """Класс обращается к БД и получить список всех валют"""

    def get_cureencies(self):
        # Построение пути к базе данных относительно текущего файла
        db_path = os.path.join(os.path.dirname(__file__), 'dataBase/currencies.db')
        with sqlite3.connect(db_path) as con:
            cur = con.cursor()

            cur.execute("SELECT * FROM currencies")
            result = cur.fetchall()

            data = []
            for row in result:
                data.append({
                    "id": row[0],
                    "code": row[1],
                    "name": row[2],
                    "sign": row[3]
                })

            return data


if __name__ == '__main__':
    print(CureenciesRepository().get_cureencies())
