from dto.currencyRegistrationDTO import CurrencyRegistrationDTO


class ExchangeRateRegistrationDTO:
    def __init__(self, base_currency: CurrencyRegistrationDTO = None, target_currency: CurrencyRegistrationDTO = None,
                 rate: float = None):
        self.baseCurrency = base_currency
        self.targetCurrency = target_currency
        self.rate = rate
