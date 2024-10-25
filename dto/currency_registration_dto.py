from dataclasses import dataclass


@dataclass
class CurrencyRegistrationDTO:
    name: str = None
    code: str = None
    sign: str = None
