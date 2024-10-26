from dataclasses import dataclass

from model.currency_model import CurrencyModel


@dataclass
class ExchangeRateModel:
    id: str = None
    baseCurrency: CurrencyModel = None
    targetCurrency: CurrencyModel = None
    rate: str = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "baseCurrency": self.baseCurrency.to_dict(),
            "targetCurrency": self.targetCurrency.to_dict(),
            "rate": self.rate
        }
