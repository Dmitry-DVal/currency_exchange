import json


class JsonFormater:
    "Преобразует данные в json"

    def to_json(self, data):
        # Проверяем, если данные — это список (например, для валют), обрабатываем их
        if isinstance(data, list):
            result = self.make_dict(data)
            return json.dumps(result, indent=4)
        else:
            # Если это словарь или ошибка, возвращаем его напрямую
            return json.dumps(data)

    @staticmethod
    def make_dict(data):
        result = []
        for row in data:
            result.append({
                "id": row[0],
                "code": row[1],
                "name": row[2],
                "sign": row[3]
            })
        return result
