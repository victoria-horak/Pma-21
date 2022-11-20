from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

class HTTP_HANDLER(BaseHTTPRequestHandler):
    def _set_response(self,response_text = "Hi"):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_text.encode('UTF-8'))
    def do_GET(self):
        self._set_response("Hello user")
    def do_POST(self):
        response_name = ''
        path = parse_qs(urlparse(self.path).query)
        if(path.get('name',0) != 0):
            response_name = path.get('name','user')
            if(response_name != 'user'):
                response_name = response_name[0]
            response_name = f'Hi {response_name} from Params\n'

        if(self.headers.get('name',0)):
            response_name += f"Hi {self.headers.get('name','user')} from Header\n"

        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        if(post_body):
                response_name += f"Hi {json.loads(post_body).get('name','user')} from body\n"
            
        self._set_response(response_name)

def run(server_class=HTTPServer, handler_class=HTTP_HANDLER, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()



run()