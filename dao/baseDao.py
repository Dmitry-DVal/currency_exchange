from myExceptions import *
from model.currencyModel import CurrencyModel


class BaseDao:
    def make_currency_model_response(self, data: list) -> CurrencyModel:
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
