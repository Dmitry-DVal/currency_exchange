from model.currencyModel import CurrencyModel

from dto import ExchangeCurrencyDTO
from dao import CurrencyDao, ExchangeRateDao


class CurrenciesService:
    def __init__(self, dto=None):
        self.dto = dto

    def get_currencies(self) -> dict or Exception:
        try:
            result = CurrencyDao().get_currencies()
            currencies = self.make_currencies_dict(result)
            return currencies
        except Exception as error:
            raise error

    def get_exchangerates(self) -> dict or Exception:
        try:
            result = ExchangeRateDao().get_exchange_rates()
            exchange_rates = self.make_exchange_rates_dict(result)
            return exchange_rates
        except Exception as error:
            raise error

    def get_exchange_currency(self) -> ExchangeCurrencyDTO or Exception:
        try:
            exchange, converted_amount = self.get_direct_exchange_rate()
            exchange_currency_dto = ExchangeCurrencyDTO(exchange.baseCurrency, exchange.targetCurrency, exchange.rate,
                                                        self.dto.amount, converted_amount)
            return exchange_currency_dto
        except Exception:
            pass
        try:
            exchange, rate, converted_amount = self.get_reverse_exchange_rate()
            exchange_currency_dto = ExchangeCurrencyDTO(exchange.targetCurrency, exchange.baseCurrency, rate,
                                                        self.dto.amount, converted_amount)
            return exchange_currency_dto
        except Exception:
            pass
        try:
            base_currency, target_currency, rate, converted_amount = self.get_cross_usd_rate()
            exchange_currency_dto = ExchangeCurrencyDTO(base_currency, target_currency, rate,
                                                        self.dto.amount, converted_amount)
            return exchange_currency_dto
        except Exception as error:
            raise error

    def get_direct_exchange_rate(self):
        exchange_rate = ExchangeRateDao(self.dto).get_exchange_rate(self.dto.baseCurrency.code,
                                                                    self.dto.targetCurrency.code)
        converted_amount = round(self.dto.amount * exchange_rate.rate, 2)

        return exchange_rate, converted_amount

    def get_reverse_exchange_rate(self):
        exchange_rate = ExchangeRateDao(self.dto).get_exchange_rate(self.dto.targetCurrency.code,
                                                                    self.dto.baseCurrency.code)
        rate = round(1 / exchange_rate.rate, 5)
        converted_amount = round(self.dto.amount * rate, 2)
        return exchange_rate, rate, converted_amount

    def get_cross_usd_rate(self):
        exchange_rate_USD_A = ExchangeRateDao(self.dto).get_exchange_rate("USD", self.dto.baseCurrency.code)
        exchange_rate_USD_B = ExchangeRateDao(self.dto).get_exchange_rate("USD", self.dto.targetCurrency.code)
        rate = round(exchange_rate_USD_B.rate / exchange_rate_USD_A.rate, 5)
        converted_amount = round(self.dto.amount * rate, 2)
        return exchange_rate_USD_A.targetCurrency, exchange_rate_USD_B.targetCurrency, rate, converted_amount

    def make_currency_model(self):
        return CurrencyModel(name=self.dto.name, code=self.dto.code, sign=self.dto.sign)  # currencyModel


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