import json


class JsonFormater:
    """Преобразует данные в json"""

    def to_json(self, data):
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
        # # Если данные пустые или None, возвращаем сообщение об отсутствии данных
        # if self.is_exchange_rates(data[0]):  # Нужна нормальная проверка
        #     print(data, type(data))
        #     result = self.make_rates_dict(data)
        #     return json.dumps(result, indent=4)
        # elif isinstance(data, list):
        #     result = self.make_currency_dict(data)
        #     return json.dumps(result, indent=4)
        # else:
        #     # Если это словарь или ошибка, возвращаем его напрямую
        #     return json.dumps(data)

    @staticmethod
    def is_exchange_rates(item):
        """Проверяет, является ли запись о курсе валют"""
        return len(item) == 10 and isinstance(item[9], (float, int))

    @staticmethod
    def make_currency_dict(data):
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
    def make_rates_dict(data):
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
