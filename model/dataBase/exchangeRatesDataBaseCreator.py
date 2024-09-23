import sqlite3


class ExchangeRatesDataBaseCreator():
    """
    Создает таблицу exchange_rates, если она ещё не создана
    """

    def __init__(self, exchangeRates):
        self.create_bd(exchangeRates)

    def create_bd(self, exchangeRates):
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

            cur.executemany("INSERT INTO exchange_rates VALUES(NULL, ?, ?, ?)", exchangeRates)


if __name__ == '__main__':
    # Начальные данные для обменных курсов валют
    exchangeRates = [(1, 2, 0.00984),
                     (2, 1, 101.62),
                     (1, 5, 0.89967),
                     (5, 2, 91.29),
                     (5, 3, 2.7),
                     (5, 4, 7.14),
                     (5, 1, 1.11)]
    ExchangeRatesDataBaseCreator(exchangeRates)
