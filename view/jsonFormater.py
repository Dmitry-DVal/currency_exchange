import json
from model.exchangeRatesRepository import ExchangeRatesRepository


class JsonFormater:
    """Преобразует данные в json"""

    def to_json(self, data):
        # Проверяем, если данные — это список (например, для валют), обрабатываем их
        if isinstance(data, list) and len(data[0]) > 6: # Нужна нормальная проверка
            result = self.make_rates_dict(data)
            return json.dumps(result, indent=4)
        elif isinstance(data, list):
            result = self.make_currency_dict(data)
            return json.dumps(result, indent=4)
        else:
            # Если это словарь или ошибка, возвращаем его напрямую
            return json.dumps(data)

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
