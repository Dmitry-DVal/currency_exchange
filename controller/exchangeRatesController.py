from http.server import BaseHTTPRequestHandler

from controller.baseController import BaseController
from controller.validator import Validator
from service.exchangeRateService import ExchangeRateService
class ExchangeRatesController(BaseController):
    """Обработка запросов по пути '/exchangeRates'"""
    def handle_get(self: BaseHTTPRequestHandler):
        try:
            response = ExchangeRateService().get_exchangerates()
            BaseController.send_response(self, response, 200)
        except Exception as e:
            BaseController.error_handler(self, e)


    def handle_post(self: BaseHTTPRequestHandler):
        print("I'm working on POST /exchangeRates")


# GET /exchangeRates
# POST /exchangeRates body - baseCurrencyCode, targetCurrencyCode, rate


# import urllib.parse
#
# from dto.currencyRegistrationDTO import CurrencyRegistrationDTO
# from dao.currencyDao import CurrencyDao
# from service.currenciesService import CurrenciesService
#
#
# class CurrenciesController(BaseController):
#     """Обработка запросов по пути '/currencies'"""
#
#     def handle_post(self: BaseHTTPRequestHandler):
#         content_length = int(self.headers['Content-Length'])  # Получаем длину содержимого
#         post_data = self.rfile.read(content_length).decode('utf-8')  # Читаем и декодируем данные
#
#         data = urllib.parse.parse_qs(post_data)
#
#         if not Validator().is_currency_fields(data):
#             error_message = 'The required form field is missing'
#             BaseController.send_response(self, {'message': error_message}, 400)
#             return
#
#         currency_dto = CurrencyRegistrationDTO(name=data.get('name')[0],
#                                                code=data.get('code')[0],
#                                                sign=data.get('sign')[0])
#         try:
#             response = CurrencyDao(
#                 currency_dto).add_currency()
#             BaseController.send_response(self, response.__dict__, 200)
#         except Exception as e:
#             BaseController.error_handler(self, e)
#
#     @staticmethod
#     def handle_get(handler: BaseHTTPRequestHandler):
#         try:
#             response = CurrenciesService().get_currencies()
#             BaseController.send_response(handler, response, 200)
#         except Exception as e:
#             BaseController.error_handler(handler, e)
