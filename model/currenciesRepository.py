import sqlite3


class CureenciesRepository:
    """Класс обращается к БД и получить список всех валют"""

    def get_ureencies(self):
        with sqlite3.connect("dataBase/currencies.db") as con:
        #with sqlite3.connect("C:/Users/mitya/OneDrive/Рабочий стол/Развитие/01 IT/00PetProjects/04_Сurrency_exchange/dataBase/currencies.db") as con:

            cur = con.cursor()

            cur.execute("SELECT * FROM currencies")
            result = cur.fetchall()
            print(result)


if __name__ == '__main__':
    CureenciesRepository().get_ureencies()
