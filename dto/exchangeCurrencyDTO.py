from dataclasses import dataclass

from model import CurrencyModel
@dataclass
class ExchangeCurrencyDTO:
    baseCurrency: CurrencyModel
    targetCurrency: CurrencyModel
    rate: float
    amount: float
    convertedAmount: float

    def to_dict(self) -> dict:
        return {
            "baseCurrency": self.baseCurrency.__dict__,
            "targetCurrency": self.targetCurrency.__dict__,
            "rate": self.rate,
            "amount": self.amount,
            "convertedAmount": self.convertedAmount
        }





