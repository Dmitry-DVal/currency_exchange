import sqlite3


class ExchangeRatesDataBaseCreator:
    """
    Создает таблицу exchange_rates, если она ещё не создана
    """

    def __init__(self, exchange_rates):
        self.create_bd(exchange_rates)

    @staticmethod
    def create_bd(exchange_rates):
        """Создает таблицу exchange_rates, если она ещё не создана."""
        with sqlite3.connect('currencies.db') as con:
            cur = con.cursor()

            # Создать таблицу, если она не существует
            cur.execute("""CREATE TABLE IF NOT EXISTS exchange_rates
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            BaseCurrencyId INTEGER,
            TargetCurrencyId INTEGER,
            Rate DECIMAL(6),
            FOREIGN KEY(BaseCurrencyId) REFERENCES currencies(ID),
            FOREIGN KEY(TargetCurrencyId) REFERENCES currencies(ID),
            UNIQUE(BaseCurrencyId, TargetCurrencyId))
            """)

            cur.executemany("INSERT OR IGNORE INTO exchange_rates VALUES(NULL, ?, ?, ?)", exchange_rates)


if __name__ == '__main__':
    # Начальные данные для обменных курсов валют
    exchange_rates = [(1, 2, 104.4),
                      (2, 1, 0.00958),
                      (1, 5, 1.09),
                      (5, 2, 96.09),
                      (5, 3, 2.73),
                      (5, 4, 7.11),
                      (5, 1, 0.92108)]
    ExchangeRatesDataBaseCreator(exchange_rates)
