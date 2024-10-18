import os
from myExceptions import *
from model.exchangeRateModel import ExchangeRateModel
from dao.baseDao import BaseDao
from dao import SQLqueries


class ExchangeRateDao(BaseDao):
    def __init__(self, exchange_rate: ExchangeRateModel = None):
        self.exchange_rate = exchange_rate
        # Построение пути к базе exchange_rate относительно текущего файла
        self.db_path = os.path.join(os.path.dirname(__file__), 'dataBase/currencies.db')

    def get_exchange_rate(self, base_currency_code: str, target_currency_code: str):
        query = SQLqueries.get_exchange_rate
        result = self._execute_query(query, (base_currency_code, target_currency_code))
        currency_model = self.make_exchange_rate_model_response(result)
        return currency_model

    def make_exchange_rate_model_response(self, data: list) -> ExchangeRateModel:
        if data:
            base_currency_model = self.make_currency_model_response([data[0][1:5]])
            target_currency_model = self.make_currency_model_response([data[0][5:-1]])
            exchange_rate_model = ExchangeRateModel(data[0][0], base_currency_model, target_currency_model,
                                                    data[0][9])
            return exchange_rate_model
        else:
            raise ExchangeRateNotFoundError

    def update_exchange_rate(self):
        """Обновляет обменный курс в БД."""
        query = SQLqueries.update_exchange_rate
        self._execute_query(query, (self.exchange_rate.rate,
                                    self.exchange_rate.baseCurrency.code, self.exchange_rate.targetCurrency.code))
        query = SQLqueries.get_exchange_rate
        result = self._execute_query(query,
                                     (self.exchange_rate.baseCurrency.code, self.exchange_rate.targetCurrency.code))
        currency_model = self.make_exchange_rate_model_response(result)
        print(currency_model.to_dict(), 'Вот и обновили')
        return currency_model

    def get_exchange_rates(self):
        """Получает список обменных курсов"""
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()

            cur.execute(SQLqueries.get_exchange_rates)
            result = cur.fetchall()
            return result
