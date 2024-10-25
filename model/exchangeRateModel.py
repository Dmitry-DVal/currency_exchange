from dataclasses import dataclass
from model.currencyModel import CurrencyModel


@dataclass
class ExchangeRateModel:
    id: str = None
    baseCurrency: CurrencyModel = None
    targetCurrency: CurrencyModel = None
    rate: float = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "baseCurrency": self.baseCurrency.__dict__,
            "targetCurrency": self.targetCurrency.__dict__,
            "rate": self.rate
        }
