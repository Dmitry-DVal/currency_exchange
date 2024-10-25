from dataclasses import dataclass

from dto.currencyRegistrationDTO import CurrencyRegistrationDTO

@dataclass
class ExchangeRateRegistrationDTO:
    baseCurrency: CurrencyRegistrationDTO | None
    targetCurrency: CurrencyRegistrationDTO | None
    rate: float
