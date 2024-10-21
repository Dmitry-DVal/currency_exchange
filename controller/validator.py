class Validator:

    @staticmethod
    def is_currency_fields(data: dict) -> bool:
        """Проверяет что все необходимые поля присутствуют в запросе"""
        required_fields = ['name', 'code', 'sign']
        return all(f in data for f in required_fields)

    @staticmethod
    def is_exchange_rates_fields(data: dict) -> bool:
        """Проверяет что все необходимые поля присутствуют в запросе"""
        required_fields = ['baseCurrencyCode', 'targetCurrencyCode', 'rate']
        try:
            return all(f in data for f in required_fields) and isinstance((float(data['rate'][0])), float)
        except ValueError:
            return False

    @staticmethod
    def is_exchange_rate_field(data: dict) -> bool:
        """Проверяет что все необходимые поля присутствуют в запросе"""
        try:
            return 'rate' in data and isinstance((float(data['rate'][0])), float)
        except ValueError:
            return False

    @staticmethod
    def is_exchange_fields(data: str) -> dict or False:
        """Проверяет что все необходимые поля присутствуют в запросе"""
        try:
            result = Validator.convert_exchange_to_dict(data)
            required_fields = ['from', 'to', 'amount']
            return result if (
                        all(field in result for field in required_fields) and isinstance((float(result['amount'])),
                                                                                         float)) else False
        except ValueError:
            return False


    @staticmethod
    def convert_exchange_to_dict(data: str) -> dict or False:
        """Форматирует полученный запрос в словарь"""
        result = {}
        for i in data.split('&'):
            key, value = i.split('=')
            result[key.replace('/exchange?', '')] = value
        return result
