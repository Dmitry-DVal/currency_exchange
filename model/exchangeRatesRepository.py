import sqlite3
import os
import json


class ExchangeRatesRepository:
    """Класс для обращения к таблице ExchangeRates"""

    def __init__(self):
        # Построение пути к базе данных относительно текущего файла
        self.db_path = os.path.join(os.path.dirname(__file__), 'dataBase/currencies.db')

    def get_exchange_rates(self):
        """Получает список обменных курсов"""
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()

            cur.execute("""SELECT
er.ID AS exchange_rate_id,

bc.ID AS base_currency_id,
bc.FullName AS base_currency_name,
bc.Code AS base_currency_code,
bc.Sign  AS base_currency_sign,

tc.ID AS target_currency_id,
tc.FullName AS target_currency_name,
tc.Code AS target_currency_code,
tc.Sign As target_currency_sign,

er.Rate

FROM exchange_rates AS er
JOIN currencies AS bc ON er.BaseCurrencyId = bc.ID
JOIN currencies AS tc ON er.TargetCurrencyId = tc.ID""")
            result = cur.fetchall()
            print(result, type(result))  # Проверяем как выводится информация
            return result


def get_exchange_rates():
    db_path = 'dataBase/currencies.db'  # Укажи путь к базе данных
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        query = """
        SELECT
er.ID AS id
FROM exchange_rates AS er 
        """
        cur.execute(query)
        rows = cur.fetchall()

        print(rows)

        # Преобразование в нужный формат
        result = []
        for row in rows:
            result.append({
                "id": row[0],
                "baseCurrency": {
                    "id": row[1],
                    "name": row[2],
                    "code": row[3],
                    "sign": row[4]
                },
                "targetCurrency": {
                    "id": row[5],
                    "name": row[6],
                    "code": row[7],
                    "sign": row[8]
                },
                "rate": row[9]
            })

        return json.dumps(result, indent=4)  # Преобразование в JSON-формат


if __name__ == '__main__':
    ExchangeRatesRepository().get_exchange_rates()
