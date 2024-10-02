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

    @staticmethod
    def get_exchange(handler: BaseHTTPRequestHandler, path: str):
        exchange_dict = GetHandler.convert_exchange_to_dict(path)
        print("Вот какой словарь выходит:")
        print(exchange_dict)
        # Проверка, что необходимые поля существуют
        if not GetHandler.check_exchange_fields(exchange_dict):
            ResponseHandler.bad_request_400(handler, 'Required form field is missing or amount is not digit')
            return

        # Проверка, существуют ли обе валюты
        if not CurrencyRepository(exchange_dict['from']).currency_exists() or not CurrencyRepository(
                exchange_dict['to']).currency_exists():
            ResponseHandler.currency_not_found(handler, 'One or both currencies are not in the database')
            return

        # Три сценария получения обменного курса
        # Есть прямой курс: AB
        # http://localhost:8000//exchange?from=USD&to=RUB&amount=10
        if ExchangeRatesRepository().exchange_rates_exists({'baseCurrencyCode': exchange_dict['from'],
                                                            'targetCurrencyCode': exchange_dict['to']}):
            print(f'Есть прямой курс для {exchange_dict["from"], exchange_dict["to"]}')
        # Есть обратный курс:
        # http://localhost:8000//exchange?from=RUB&to=USD&amount=10
        elif ExchangeRatesRepository().exchange_rates_exists({'baseCurrencyCode': exchange_dict['to'],
                                                              'targetCurrencyCode': exchange_dict['from']}):
            print(f'Прямого курс для {exchange_dict["from"], exchange_dict["to"]} - нет')
            print(f'Есть курс для {exchange_dict["to"], exchange_dict["from"]}')
        # Есть курс через доллар
        # http://localhost:8000//exchange?from=GEL&to=RUB&amount=10
        elif (ExchangeRatesRepository().exchange_rates_exists({'baseCurrencyCode': 'USD',
                                                              'targetCurrencyCode': exchange_dict['from']})
              and ExchangeRatesRepository().exchange_rates_exists({'baseCurrencyCode': 'USD',
                                                                   'targetCurrencyCode': exchange_dict['to']})):
            print(f'Прямого и обратного курсов для {exchange_dict["from"], exchange_dict["to"]} - нет')
            print(f'Есть курс для USD-{exchange_dict["from"]} и USD-{exchange_dict["to"]}')
        else:
            ResponseHandler.currency_not_found(handler)

    @staticmethod
    def convert_exchange_to_dict(data: str) -> dict:
        """Форматирует полученный запрос в словарь"""
        result = {}
        for i in data.split('&'):
            key, value = i.split('=')
            result[key.replace('/exchange?', '')] = value
        return result

    @staticmethod
    def check_exchange_fields(your_dict: dict) -> bool:
        """Проверяет что все необходимые поля присутствуют в запросе"""
        required_fields = ['from', 'to', 'amount']
        # Проверяем наличие всех полей
        if not all(field in your_dict for field in required_fields):
            return False
        # Преобразуем amount в число и проверяем, что это положительное число
        try:
            rate = float(your_dict['amount'])
            if rate <= 0:
                return False
        except ValueError:
            return False
        return True
