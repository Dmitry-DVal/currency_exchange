from dao.exchangeRateDao import ExchangeRateDao


class ExchangeRateService:
    def get_exchangerates(self) -> dict or Exception:
        try:
            result = ExchangeRateDao().get_exchange_rates()
            exchange_rates = self.make_exchange_rates_dict(result)
            return exchange_rates
        except Exception as error:
            raise error

    @staticmethod
    def make_exchange_rates_dict(data: list) -> list:
        result = []
        for exchange_rate_model in data:
            result.append(exchange_rate_model.to_dict())
        return result
