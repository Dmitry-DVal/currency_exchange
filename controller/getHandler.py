from model.currenciesRepository import CureenciesRepository
from model.currencyRepository import CurrencyRepository
from model.exchangeRatesRepository import ExchangeRatesRepository
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
        exchange_rates = ExchangeRatesRepository().get_exchange_rates()  # [(1, 1, 2, 0.00984), (2, 2, 1, 101.62), (3, 1, 5, 0.89967), (4, 5, 2, 91.29), (5, 5, 3, 2.7), (6, 5, 4, 7.14), (7, 5, 1, 1.11)]
        ResponseHandler.good_request_200(handler, exchange_rates)