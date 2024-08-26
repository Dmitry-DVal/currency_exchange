from http.server import HTTPServer
from ourHandler import OurHandler

port = 8000

if __name__ == "__main__":
    with HTTPServer(('', port), OurHandler) as server:
        server.serve_forever()