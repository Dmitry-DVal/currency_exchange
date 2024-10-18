class CurrencyRegistrationDTO:
    def __init__(self, name: str = None, code: str = None, sign: str = None):
        self.name = name
        self.code = code
        self.sign = sign
