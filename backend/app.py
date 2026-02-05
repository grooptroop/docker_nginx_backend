from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')  
            self.end_headers()
            self.wfile.write(b'Hello from Effective Mobile!')  


if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), Handler)
    server.serve_forever()