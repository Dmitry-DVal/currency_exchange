from http.server import BaseHTTPRequestHandler
from controller.baseController import BaseController
from service.exchangeRateService import ExchangeRateService

from service.currenciesService import CurrenciesService
import urllib.parse
class ExchangeRateController(BaseController):
    """Обработка запросов по пути '/exchangeRate"""
    # def __init__(self):
    #     self.baseCurrency = BaseHTTPRequestHandler.path.split('/')[-1]
    #     self.targetCurrency = BaseHTTPRequestHandler.path.split('/')[-1]

    @staticmethod
    def handle_get(handler: BaseHTTPRequestHandler): # /exchangeRate/USDRUB
        print("I'm working on GET request")
        path_parts = handler.path.split('/') # ['', 'exchangeRate', 'RUBUSD']
        print(path_parts, type(path_parts))
        base_currency, target_currency = path_parts[2][:3], path_parts[2][3:] # RUB USD
        print(base_currency, target_currency)
        exchange_rate = ExchangeRateService.get_exchange_rate(base_currency, target_currency)
        BaseController.send_response(handler, exchange_rate, 200)
        # baseCurrency = handler.BaseHTTPRequestHandler.path.split('/')[-1]
        # print(f"{baseCurrency}")
        # try:
        #     response = CurrenciesService.get_exchange_rate()
        #     BaseController.send_response(handler, response, 200)
        # except Exception as e:
        #     BaseController.error_handler(handler, e)

    @staticmethod
    def handle_patch(handler: BaseHTTPRequestHandler): # /exchangeRate/USDRUB bode rate
        print("I'm working on PATCH request")
# Извлечь коды базовой валюты и целевой валюты из URL.
# Проверить, что тело запроса содержит обновленный курс (rate).
# Обновить запись в базе данных, если такая валютная пара существует.
# Вернуть обновленную запись, если она успешно обновлена, или отправить ошибку, если что-то пошло не так.



# from dto.currencyRegistrationDTO import CurrencyRegistrationDTO
# from controller.validator import Validator
#
#
# class CurrenciesController(BaseController):
#     """Обработка запросов по пути '/currencies'"""
#
#     @staticmethod
#     def handle_post(handler: BaseHTTPRequestHandler):
#         content_length = int(handler.headers['Content-Length'])  # Получаем длину содержимого
#         post_data = handler.rfile.read(content_length).decode('utf-8')  # Читаем и декодируем данные
#
#         data = urllib.parse.parse_qs(post_data)  # {'name': ['Mavrod'], 'code': ['MYR'], 'sign': ['M']}
#
#         if not Validator().check_currency_fields(data):
#             error_message = 'The required form field is missingt'
#             BaseController.send_response(handler, {'message': error_message}, 400)
#             return
#
#         currency_dto = CurrencyRegistrationDTO(data.get('name')[0], data.get('code')[0], data.get('sign')[0])
#         try:
#             service = CurrenciesService(currency_dto)
#             response = service.add_currency_to_db()
#             BaseController.send_response(handler, response, 200)
#         except Exception as e:
#             BaseController.error_handler(handler, e)
#
#     @staticmethod
#     def handle_get(handler: BaseHTTPRequestHandler):
#         try:
#             response = CurrenciesService.get_currencies()
#             BaseController.send_response(handler, response, 200)
#         except Exception as e:
#             BaseController.error_handler(handler, e)
