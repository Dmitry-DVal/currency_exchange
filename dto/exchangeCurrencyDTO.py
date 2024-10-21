class ExchangeCurrencyDTO:
    def __init__(self, base_currency: tuple, target_currency: tuple,
                 rate: float, amount: float, converted_amount: float):
        self.baseCurrency = base_currency.__dict__
        self.targetCurrency = target_currency.__dict__
        self.rate = rate
        self.amount = amount
        self.converted_amount = converted_amount

    def to_dict(self) -> dict:
        return {
            "baseCurrency": self.baseCurrency.__dict__,
            "targetCurrency": self.targetCurrency.__dict__,
            "rate": self.rate,
            "amount": self.amount,
            "convertedAmount": self.converted_amount
        }
