from dao.exchangeRateDao import ExchangeRateDao
class ExchangeRateService:
    @staticmethod
    def get_exchange_rate(base_currency, target_currency):
        # Получаем курс из базы данных
        exchange_rate = ExchangeRateDao.get_exchange_rate(base_currency, target_currency)
        if not exchange_rate:
            raise CurrencyNotFoundError("Exchange rate not found")

        return {
            'id': exchange_rate.id,
            'baseCurrency': {
                'id': exchange_rate.base_currency_id,
                'name': exchange_rate.base_currency_name,
                'code': exchange_rate.base_currency_code,
                'sign': exchange_rate.base_currency_sign
            },
            'targetCurrency': {
                'id': exchange_rate.target_currency_id,
                'name': exchange_rate.target_currency_name,
                'code': exchange_rate.target_currency_code,
                'sign': exchange_rate.target_currency_sign
            },
            'rate': exchange_rate.rate
        }

