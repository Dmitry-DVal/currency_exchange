import os
import sqlite3

import my_exceptions
from model import CurrencyModel, ExchangeRateModel


class BaseDao:
    def __init__(self):
        self._db_path = os.path.join(
            os.path.dirname(__file__), "dataBase/currencies.db"
        )

    def make_currency_model_response(self, data: list) -> CurrencyModel:
        if data:
            currency_model = CurrencyModel(
                data[0][0], data[0][1], data[0][2], data[0][3]
            )
            return currency_model
        raise my_exceptions.CurrencyNotFoundError

    def _execute_query(self, query, params=()):
        try:
            with sqlite3.connect(self._db_path) as con:
                cur = con.cursor()
                if params:
                    cur.execute(query, params)
                else:
                    cur.execute(query)
                return cur.fetchall()
        except sqlite3.IntegrityError:
            raise my_exceptions.CurrencyCodeError(
                "Currency code is not unique or does not match the format"
            )
        except sqlite3.OperationalError:
            raise my_exceptions.DatabaseUnavailableError("Database unavailable")

    def make_exchange_rate_model_response(self, data: list) -> ExchangeRateModel:
        if data:
            base_currency_model = self.make_currency_model_response([data[0][1:5]])
            target_currency_model = self.make_currency_model_response([data[0][5:-1]])
            exchange_rate_model = ExchangeRateModel(
                data[0][0], base_currency_model, target_currency_model, data[0][9]
            )
            return exchange_rate_model
        raise my_exceptions.ExchangeRateNotFoundError
