from model.currencyModel import CurrencyModel


class ExchangeRateModel:
    def __init__(self, id: str = None, baseCurrency: CurrencyModel = None, targetCurrency: CurrencyModel = None,
                 rate: str = None):
        self.id = id
        self.baseCurrency = baseCurrency
        self.targetCurrency = targetCurrency
        self.rate = rate

    def to_dict(self):
        return {
            "id": self.id,
            "baseCurrency": self.baseCurrency.__dict__,
            "targetCurrency": self.targetCurrency.__dict__,
            "rate": self.rate
        }

