# angle_service.py
import http.server
import socketserver
import json
import time

start_time = time.time()

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/angle':
            angle = (time.time() - start_time) * 90 % 360
            data = {"angle": angle}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.end_headers()

print("Angle service запущен на http://127.0.0.1:8000")
socketserver.TCPServer(("0.0.0.0", 8000), Handler).serve_forever()