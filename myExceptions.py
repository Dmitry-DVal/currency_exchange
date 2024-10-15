import sqlite3


class CurrencyCodeError(sqlite3.IntegrityError):
    """Исключение для ошибки уникальности кода валюты."""
    pass


class DatabaseUnavailableError(sqlite3.OperationalError):
    """Исключение при недоступности БД."""
    pass
