from dataclasses import dataclass

from dto.currency_registration_dto import CurrencyRegistrationDTO


@dataclass
class ExchangeRateRegistrationDTO:
    baseCurrency: CurrencyRegistrationDTO | None
    targetCurrency: CurrencyRegistrationDTO | None
    rate: float
