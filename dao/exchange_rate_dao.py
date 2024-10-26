from dao import sql_queries
from dao.base_dao import BaseDao
from model.exchange_rate_model import ExchangeRateModel


class ExchangeRateDao(BaseDao):
    def __init__(self, exchange_rate: ExchangeRateModel = None):
        super().__init__()
        self.exchange_rate = exchange_rate

    def get_exchange_rate(self, base_currency_code: str, target_currency_code: str):
        query = sql_queries.get_exchange_rate
        result = self._execute_query(query, (base_currency_code, target_currency_code))
        currency_model = self.make_exchange_rate_model_response(result)
        return currency_model

    def update_exchange_rate(self):
        """Обновляет обменный курс в БД."""
        query = sql_queries.update_exchange_rate
        self._execute_query(
            query,
            (
                self.exchange_rate.rate,
                self.exchange_rate.baseCurrency.code,
                self.exchange_rate.targetCurrency.code,
            ),
        )
        query = sql_queries.get_exchange_rate
        result = self._execute_query(
            query,
            (
                self.exchange_rate.baseCurrency.code,
                self.exchange_rate.targetCurrency.code,
            ),
        )
        currency_model = self.make_exchange_rate_model_response(result)
        return currency_model

    def get_exchange_rates(self) -> list[ExchangeRateModel]:
        """Получает список обменных курсов"""
        query = sql_queries.get_exchange_rates
        result = self._execute_query(query)
        response = []
        for exchange_rate in result:
            response.append(self.make_exchange_rate_model_response([exchange_rate]))
        return response

    def add_exchange_rate(self):
        """Добавляет обменный курс в БД."""
        query = sql_queries.add_exchange_rate
        self._execute_query(
            query,
            (
                self.exchange_rate.baseCurrency.code,
                self.exchange_rate.targetCurrency.code,
                self.exchange_rate.rate,
            ),
        )
        query = sql_queries.get_exchange_rate
        result = self._execute_query(
            query,
            (
                self.exchange_rate.baseCurrency.code,
                self.exchange_rate.targetCurrency.code,
            ),
        )
        currency_model = self.make_exchange_rate_model_response(result)
        return currency_model
