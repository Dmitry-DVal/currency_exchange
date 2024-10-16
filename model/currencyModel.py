from dataclasses import dataclass

@dataclass
class CurrencyModel:
    name: str
    code: str
    sign: str
    id: str = None

