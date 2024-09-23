from http.server import HTTPServer
from controller.ourHandler import OurHandler

port = 8000

if __name__ == "__main__":
    with HTTPServer(('', port), OurHandler) as server:
        server.serve_forever()

# корректный запрос на добавление валюты
# curl -X POST http://localhost:8000/currencies -d "name=Albanian Lek&code=ALL&sign=L" -H "Content-Type: application/x-www-form-urlencoded"
