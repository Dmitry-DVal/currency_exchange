from http.server import HTTPServer
from controller.ourHandler import OurHandler

port = 8000

if __name__ == "__main__":
    with HTTPServer(('', port), OurHandler) as server:
        server.serve_forever()

# корректный POST запрос на добавление валюты в curl
# curl -X POST http://localhost:8000/currencies -d "name=Albanian Lek&code=ALL&sign=L" -H "Content-Type: application/x-www-form-urlencoded"

# GET запросы можно также отправлять через curl или через браузер, пример для браузера
# http://localhost:8000/currencies
# http://localhost:8000/currency/RUB

