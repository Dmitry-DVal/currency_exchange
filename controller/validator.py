class Validator:

    @staticmethod
    def check_currency_fields(data: dict) -> bool:
        """Проверяет что все необходимые поля присутствуют в запросе"""
        required_fields = ['name', 'code', 'sign']
        return all(f in data for f in required_fields)
