import json

class JsonFormater:

    @staticmethod
    def to_json(data):
        return json.dumps(data)
