from http.server import BaseHTTPRequestHandler
from model.currencyRepository import CurrencyRepository
from model.exchangeRatesRepository import ExchangeRatesRepository
from controller.responseHandler import ResponseHandler
import sqlite3


class PatchHandler:
    """Обработчик PATCH запросов"""

    @staticmethod
    def patch_exchange_rate(self, base_currency_code, target_currency_code):
        pass
        # Проверка наличия поля rate 400 если нет поля
        # Проверка есть ли вообще такие валюты в таблице куренсис. Не вижу смысла это делать
        # Если валюты есть, проверить есть данные по валютам (обменный курс) в таблице эксчейндж рейт 404
        # Если они есть - обновить даннные, прислать новые данные клиенту 200