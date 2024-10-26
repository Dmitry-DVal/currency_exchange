import sqlite3


class CurrencyCodeError(sqlite3.IntegrityError):
    """Исключение для ошибки уникальности кода валюты."""

    pass


class DatabaseUnavailableError(sqlite3.OperationalError):
    """Исключение при недоступности БД."""

    pass


class CurrencyNotFoundError(Exception):
    """Валюта не найдена."""

    pass


class ExchangeRateNotFoundError(Exception):
    """Обменный курс не найден."""

    pass
