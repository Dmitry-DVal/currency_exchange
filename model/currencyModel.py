class CurrencyModel:
    def __init__(self, name: str, code: str, sign: str, id=None):
        self.id = id
        self.name = name
        self.code = code
        self.sign = sign
