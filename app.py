from http.server import HTTPServer
from router import Router

port = 8080

if __name__ == "__main__":
    with HTTPServer(('', port), Router) as server:
        print(f"Server running on port {port}")
        server.serve_forever()