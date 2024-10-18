class Validator:

    @staticmethod
    def is_currency_fields(data: dict) -> bool:
        """Проверяет что все необходимые поля присутствуют в запросе"""
        required_fields = ['name', 'code', 'sign']
        return all(f in data for f in required_fields)

    @staticmethod
    def is_exchange_rate_field(data: dict) -> bool:
        """Проверяет что все необходимые поля присутствуют в запросе"""
        try:
            return 'rate' in data and isinstance((float(data['rate'][0])), float)
        except ValueError:
            return False


