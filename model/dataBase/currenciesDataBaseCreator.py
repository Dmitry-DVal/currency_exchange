import sqlite3


class CurrenciesDataBaseCreator():
    """
    Создает таблицу Currencies, если она ещё не создана

    """

    def __init__(self, currencies_list: list):
        self.create_bd(currencies_list)

    def create_bd(self, currencies_list: list):
        with sqlite3.connect('currencies.db') as con:
            cur = con.cursor()  # курсор

            # Создать таблицу, если она не существует
            cur.execute("""CREATE TABLE IF NOT EXISTS currencies
            (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
    Code VARCHAR(3) UNIQUE NOT NULL CHECK(LENGTH(Code) = 3 AND Code GLOB '[A-Z][A-Z][A-Z]'),
    FullName VARCHAR NOT NULL, 
    Sign VARCHAR NOT NULL)""")

            # Проверка, есть ли уже записи в таблице
            cur.execute("SELECT COUNT(*) FROM currencies")
            if cur.fetchone()[0] == 00:
                cur.executemany("INSERT INTO currencies VALUES(NULL, ?, ?, ?)", currencies_list)


if __name__ == '__main__':
    # Начальный список валют
    currencies_list = [('EUR', 'Euro', '€'),
                       ('RUB', 'Russian Ruble', '₽'),
                       ('GEL', 'Georgian Lari', '₾'),
                       ('CNY', 'Chinese Yuan ', '¥'),
                       ('USD', 'US Dollar', '$')]
    CurrenciesDataBaseCreator(currencies_list)
