from http.server import BaseHTTPRequestHandler
from controller.baseController import BaseController
from dto.currencyRegistrationDTO import CurrencyRegistrationDTO
from dao.exchangeRateDao import ExchangeRateDao


class ExchangeRateController(BaseController):
    """Обработка запросов по пути '/exchangeRate"""

    def handle_get(self: BaseController):
        try:
            path_parts = self.path.split('/')[2]  # ['', 'exchangeRate', 'RUBUSD']
            base_currency_dto, target_currency_dto = (CurrencyRegistrationDTO(code=path_parts[:3]),
                                                      CurrencyRegistrationDTO(code=path_parts[3:]),)
            exchange_rate = ExchangeRateDao().get_exchange_rate(base_currency_dto.code, target_currency_dto.code)
            BaseController.send_response(self, exchange_rate.to_dict(), 200)
        except Exception as e:
            BaseController.error_handler(self, e)

    @staticmethod
    def handle_patch(handler: BaseHTTPRequestHandler):  # /exchangeRate/USDRUB bode rate
        print("I'm working on PATCH request")
# Извлечь коды базовой валюты и целевой валюты из URL.
# Проверить, что тело запроса содержит обновленный курс (rate).
# Обновить запись в базе данных, если такая валютная пара существует.
# Вернуть обновленную запись, если она успешно обновлена, или отправить ошибку, если что-то пошло не так.
