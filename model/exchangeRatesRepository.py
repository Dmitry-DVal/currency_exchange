import sqlite3
import os


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
            return result


if __name__ == '__main__':
    ExchangeRatesRepository().get_exchange_rates()
