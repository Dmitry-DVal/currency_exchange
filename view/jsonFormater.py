import json


class JsonFormater:
    """
        Преобразует данные в JSON-строку.

        :param: Данные для преобразования в json, могут быть списком, словарем или None.
        :return: Строка в формате JSON.
        """

    def to_json(self, data) -> str:
        # Проверяем, если data пустое или None
        if not data:
            return json.dumps({"error": "No data found"})

        # Проверяем, если data — это список
        elif isinstance(data, list):
            # Проверяем, что первый элемент списка соответствует ожидаемой структуре
            if self.is_exchange_rates(data[0]):
                result = self.make_rates_dict(data)
                return json.dumps(result, indent=4)
            else:
                result = self.make_currency_dict(data)
                return json.dumps(result, indent=4)

        # Если это словарь или ошибка, возвращаем его напрямую
        return json.dumps(data)

    def transfer_currency_to_json(self, exchange_rate: list, amount: float, rate: float) -> str:
        result = []
        for row in exchange_rate:
            result.append({
                "baseCurrency": {
                    "id": row[1],
                    "name": row[2],
                    "code": row[3],
                    "sign": row[4]
                },
                "targetCurrency": {
                    "id": row[5],
                    "name": row[6],
                    "code": row[7],
                    "sign": row[8]
                },
                "rate": rate,
                "amount": amount,
                "convertedAmount": rate * float(amount)

            })
        return json.dumps(result, indent=4)

    @staticmethod
    def is_exchange_rates(item: list) -> bool:
        """Проверяет, является ли запись о курсе валют"""
        return len(item) == 10 and isinstance(item[9], (float, int))

    @staticmethod
    def make_currency_dict(data: list) -> list:
        result = []
        for row in data:
            result.append({
                "id": row[0],
                "code": row[1],
                "name": row[2],
                "sign": row[3]
            })
        return result

    @staticmethod
    def make_rates_dict(data: list) -> list:
        result = []
        for row in data:
            result.append({
                "id": row[0],
                "baseCurrency": {
                    "id": row[1],
                    "name": row[2],
                    "code": row[3],
                    "sign": row[4]
                },
                "targetCurrency": {
                    "id": row[5],
                    "name": row[6],
                    "code": row[7],
                    "sign": row[8]
                },
                "rate": row[9]

            })
        return result
