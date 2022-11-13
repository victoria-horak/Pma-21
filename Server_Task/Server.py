from http.server import HTTPServer, BaseHTTPRequestHandler


class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        # name = 'Vova'
        self.wfile.write(self.path[1:].encode())


def main():
    PORT = 10000
    server = HTTPServer(('', PORT), echoHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()  # starting the server


if __name__ == '__main__':
    main()
