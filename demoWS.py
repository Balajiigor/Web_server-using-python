from http import server
from http.server import HTTPServer,BaseHTTPRequestHandler

class host(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(self.path[1:].encode())

def main():
    PORT = 8000
    server = HTTPServer(('',PORT),host)
    print("server working on %s"%PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()