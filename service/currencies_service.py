from decimal import Decimal

from dao import CurrencyDao, ExchangeRateDao
from dto import ExchangeCurrencyDTO
from model.currency_model import CurrencyModel
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
        converted_amount = str(round(self.dto.amount * Decimal(exchange_rate.rate), 2))
        exchange_currency_dto = ExchangeCurrencyDTO(exchange_rate.baseCurrency, exchange_rate.targetCurrency,
                                                    exchange_rate.rate, str(self.dto.amount), converted_amount)
        return exchange_currency_dto

    def get_reverse_exchange_rate(self) -> ExchangeCurrencyDTO:
        exchange_rate = ExchangeRateDao(self.dto).get_exchange_rate(self.dto.targetCurrency.code,
                                                                    self.dto.baseCurrency.code)
        rate = round(1 / Decimal(exchange_rate.rate), 5)
        converted_amount = str(round(self.dto.amount * rate, 2))
        exchange_currency_dto = ExchangeCurrencyDTO(exchange_rate.targetCurrency, exchange_rate.baseCurrency, str(rate),
                                                    str(self.dto.amount), converted_amount)
        return exchange_currency_dto

    def get_cross_usd_rate(self) -> ExchangeCurrencyDTO:
        exchange_rate_usd_a = ExchangeRateDao(self.dto).get_exchange_rate("USD",
                                                                          self.dto.baseCurrency.code)
        exchange_rate_usd_b = ExchangeRateDao(self.dto).get_exchange_rate("USD",
                                                                          self.dto.targetCurrency.code)
        rate = round(Decimal(exchange_rate_usd_b.rate) / Decimal(exchange_rate_usd_a.rate), 5)
        converted_amount = str(round(self.dto.amount * rate, 2))
        exchange_currency_dto = ExchangeCurrencyDTO(exchange_rate_usd_a.targetCurrency,
                                                    exchange_rate_usd_b.targetCurrency, str(rate),
                                                    str(self.dto.amount), converted_amount)
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
