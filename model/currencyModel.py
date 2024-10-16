from dataclasses import dataclass


@dataclass
class CurrencyModel:
    id: str = None
    name: str = None
    code: str = None
    sign: str = None
