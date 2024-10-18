from model.currencyModel import CurrencyModel


class ExchangeRateRegistrationDTO:
    def __init__(self, id: str = None, baseCurrency: CurrencyModel = None, targetCurrency: CurrencyModel = None,
                 rate: int = None):
        self.id = id
        self.baseCurrency = baseCurrency
        self.targetCurrency = targetCurrency
        self.rate = rate
