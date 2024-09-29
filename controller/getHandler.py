from http.server import BaseHTTPRequestHandler
from model.currenciesRepository import CureenciesRepository
from model.currencyRepository import CurrencyRepository
from model.exchangeRatesRepository import ExchangeRatesRepository
from controller.responseHandler import ResponseHandler


class GetHandler:
    """Обработчик GET запросов"""

    @staticmethod
    def get_currencies(handler: BaseHTTPRequestHandler):
        """Отправляет клиенту список всех валют"""
        currencies = CureenciesRepository().get_cureencies()
        ResponseHandler.good_request_200(handler, currencies)

    @staticmethod
    def get_currency(handler: BaseHTTPRequestHandler, currency_code: str):
        """Отправляет клиенту конкретную валюту"""
        currency = CurrencyRepository(currency_code).get_currency()
        if not currency:
            # Если валюта не найдена, отправляем 404 ошибку
            ResponseHandler.currency_not_found(handler)
        else:
            # Если валюта найдена, возвращаем её в формате JSON
            ResponseHandler.good_request_200(handler, currency)

    @staticmethod
    def get_exchange_rates(handler: BaseHTTPRequestHandler):
        """Отправляет клиенту список всех обменных курсов"""
        exchange_rates = ExchangeRatesRepository().get_exchange_rates()
        ResponseHandler.good_request_200(handler, exchange_rates)

    @staticmethod
    def get_exchange_rate(handler: BaseHTTPRequestHandler, base_currency_code: str, target_currency_code: str):
        """Отправляет клиенту список указанного обменного курса"""
        base_currency = CurrencyRepository(base_currency_code).get_currency()
        target_currency = CurrencyRepository(target_currency_code).get_currency()

        if base_currency and target_currency:
            try:
                exchange_rate = ExchangeRatesRepository().get_exchange_rate(base_currency_code, target_currency_code)

                if not exchange_rate:  # Проверяем, что exchange_rate не пустой
                    raise KeyError("exchange rate not found")

                ResponseHandler.good_request_200(handler, exchange_rate)
            except (TypeError, KeyError) as e:
                # Обрабатываем как отсутствие данных или ошибку в структуре
                ResponseHandler.currency_not_found(handler, str(e))
        else:
            ResponseHandler.currency_not_found(handler)
