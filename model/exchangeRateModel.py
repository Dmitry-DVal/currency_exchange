from model.currencyModel import CurrencyModel


class ExchangeRateModel:
    def __init__(self, id: str = None, base_currency: CurrencyModel = None, target_currency: CurrencyModel = None,
                 rate: float = None):
        self.id = id
        self.baseCurrency = base_currency
        self.targetCurrency = target_currency
        self.rate = rate

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "baseCurrency": self.baseCurrency.__dict__,
            "targetCurrency": self.targetCurrency.__dict__,
            "rate": self.rate
        }
