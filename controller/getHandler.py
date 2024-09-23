from model.currenciesRepository import CureenciesRepository
from model.currencyRepository import CurrencyRepository
from controller.responseHandler import ResponseHandler


class GetHandler:
    """Обработчик GET запросов"""

    @staticmethod
    def get_currencies(handler):
        """Отправляет клиенту список всех валют"""
        currencies = CureenciesRepository().get_cureencies()
        ResponseHandler.good_request_200(handler, currencies)

    @staticmethod
    def get_currency(handler, currency_code):
        """Отправляет клиенту конкретную валюту"""
        currency = CurrencyRepository(currency_code).get_currency()
        if not currency:
            # Если валюта не найдена, отправляем 404 ошибку
            ResponseHandler.currency_not_found(handler)
        else:
            # Если валюта найдена, возвращаем её в формате JSON
            ResponseHandler.good_request_200(handler, currency)

    @staticmethod
    def get_exchange_rates(handler):
        """Отправляет клиенту список всех обменных курсов"""
        pass