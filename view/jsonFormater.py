import json


class JsonFormater:

    def to_json(self, data):
        result = self.make_dict(data)
        return json.dumps(result)

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
