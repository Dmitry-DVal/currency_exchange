from http.server import BaseHTTPRequestHandler

from controller.baseController import BaseController

class ExchangeController(BaseController):
    """Обработка запросов по пути 'exchange'"""

    def handle_get(self: BaseHTTPRequestHandler):
        print("I'm working on GET Exchange")
        pass
