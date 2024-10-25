from model.currency_model import CurrencyModel

from dto import ExchangeCurrencyDTO
from dao import CurrencyDao, ExchangeRateDao
from my_exceptions import *


class CurrenciesService:
    def __init__(self, dto=None):
        self.dto = dto

    def get_currencies(self) -> list:
        result = CurrencyDao().get_currencies()
        currencies = self.make_currencies_dict(result)
        return currencies

    def get_exchangerates(self) -> list:
        result = ExchangeRateDao().get_exchange_rates()
        exchange_rates = self.make_exchange_rates_dict(result)
        return exchange_rates

    def get_exchange_currency(self) -> ExchangeCurrencyDTO:
        try:
            return self.get_direct_exchange_rate()
        except ExchangeRateNotFoundError:
            try:
                return self.get_reverse_exchange_rate()
            except ExchangeRateNotFoundError:
                return self.get_cross_usd_rate()

    def get_direct_exchange_rate(self) -> ExchangeCurrencyDTO:
        exchange_rate = ExchangeRateDao(self.dto).get_exchange_rate(self.dto.baseCurrency.code,
                                                                    self.dto.targetCurrency.code)
        converted_amount = round(self.dto.amount * exchange_rate.rate, 2)
        exchange_currency_dto = ExchangeCurrencyDTO(exchange_rate.baseCurrency, exchange_rate.targetCurrency,
                                                    exchange_rate.rate, self.dto.amount, converted_amount)
        return exchange_currency_dto

    def get_reverse_exchange_rate(self) -> ExchangeCurrencyDTO:
        exchange_rate = ExchangeRateDao(self.dto).get_exchange_rate(self.dto.targetCurrency.code,
                                                                    self.dto.baseCurrency.code)
        rate = round(1 / exchange_rate.rate, 5)
        converted_amount = round(self.dto.amount * rate, 2)
        exchange_currency_dto = ExchangeCurrencyDTO(exchange_rate.targetCurrency, exchange_rate.baseCurrency, rate,
                                                    self.dto.amount, converted_amount)
        print(exchange_currency_dto)
        return exchange_currency_dto

    def get_cross_usd_rate(self) -> ExchangeCurrencyDTO:
        exchange_rate_USD_A = ExchangeRateDao(self.dto).get_exchange_rate("USD",
                                                                          self.dto.baseCurrency.code)
        exchange_rate_USD_B = ExchangeRateDao(self.dto).get_exchange_rate("USD",
                                                                          self.dto.targetCurrency.code)
        rate = round(exchange_rate_USD_B.rate / exchange_rate_USD_A.rate, 5)
        converted_amount = round(self.dto.amount * rate, 2)
        exchange_currency_dto = ExchangeCurrencyDTO(exchange_rate_USD_A.targetCurrency,
                                                    exchange_rate_USD_B.targetCurrency, rate,
                                                    self.dto.amount, converted_amount)
        return exchange_currency_dto

    def make_currency_model(self):
        return CurrencyModel(name=self.dto.name, code=self.dto.code, sign=self.dto.sign)

    @staticmethod
    def make_currencies_dict(data: list) -> list:
        result = []
        for row in data:
            result.append({
                "id": row[0],
                "name": row[2],
                "code": row[1],
                "sign": row[3]
            })
        return result

    @staticmethod
    def make_exchange_rates_dict(data: list) -> list:
        result = []
        for exchange_rate_model in data:
            result.append(exchange_rate_model.to_dict())
        return result
