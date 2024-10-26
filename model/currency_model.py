from dataclasses import dataclass


@dataclass
class CurrencyModel:
    id: str = None
    name: str = None
    code: str = None
    sign: str = None

    def to_dict(self):
        return {"id": self.id, "name": self.name, "code": self.code, "sign": self.sign}
