from http.server import HTTPServer, BaseHTTPRequestHandler

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.set_response()
        self.wfile.write(b'Hello, user!')

    def do_POST(self):
        self.set_response()
        content_length = int(self.headers['Content-Length'])
        if content_length == 0:
            self.wfile.write(b'Hello, no name user!')
        else:
            post_data = self.rfile.read(content_length)
            self.wfile.write('Hello, {}!'.format(post_data.decode('utf-8')).encode('utf-8'))


httpd = HTTPServer(('localhost', 8000), HTTPRequestHandler)
httpd.serve_forever()
