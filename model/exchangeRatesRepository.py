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

    def get_exchange_rate(self, base_currency_code: str, target_currency_code: str):
        """Получает запрашиваемый обменный курс."""
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
        JOIN currencies AS tc ON er.TargetCurrencyId = tc.ID
WHERE base_currency_code == ? AND target_currency_code == ?""", (base_currency_code, target_currency_code))

            result = cur.fetchall()
            return result

    def exchange_rates_exists(self, exchange_rates_dict):
        """Проверяет, существует ли валюта"""
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute("""SELECT * FROM exchange_rates AS er 
            JOIN currencies AS bc ON er.BaseCurrencyId = bc.ID 
            JOIN currencies AS tc ON er.TargetCurrencyId = tc.ID 
            WHERE bc.Code = ? AND tc.Code = ?""",
                        (exchange_rates_dict['baseCurrencyCode'], exchange_rates_dict['targetCurrencyCode'],))
            result = cur.fetchall()
            return bool(result)  # Если список не пустой вернет True

    def add_exchange_rate(self, exchange_rates_dict):
        """Добавляет обменный курс в БД."""
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute("""INSERT INTO exchange_rates (BaseCurrencyId, TargetCurrencyId, Rate)
VALUES (
  (SELECT ID FROM currencies WHERE Code = ?),
  (SELECT ID FROM currencies WHERE Code = ?),
  ?)""", (exchange_rates_dict['baseCurrencyCode'],
                                 exchange_rates_dict['targetCurrencyCode'],
                                 exchange_rates_dict['rate'],))


if __name__ == '__main__':
    ExchangeRatesRepository().get_exchange_rates()
