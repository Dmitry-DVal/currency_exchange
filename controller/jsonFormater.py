import json


class JsonFormater:
    """
        Преобразует данные в JSON-строку.

        :param: Данные для преобразования в json, могут быть списком, словарем или None.
        :return: Строка в формате JSON.
        """

    def to_json(self, data) -> str:
        return json.dumps(data, indent=4)

