from dataclasses import dataclass

from model import CurrencyModel


@dataclass
class ExchangeCurrencyDTO:
    baseCurrency: CurrencyModel
    targetCurrency: CurrencyModel
    rate: str
    amount: str
    convertedAmount: str

    def to_dict(self) -> dict:
        return {
            "baseCurrency": self.baseCurrency.to_dict(),
            "targetCurrency": self.targetCurrency.to_dict(),
            "rate": self.rate,
            "amount": self.amount,
            "convertedAmount": self.convertedAmount
        }





