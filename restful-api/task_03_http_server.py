#!/usr/bin/python3
"""
Set up a basic web server using the http.server module.
Handle different types of HTTP requests (GET, POST, etc.).
Serve JSON data in response to specific endpoints.
"""

import http.server
import json
import socketserver

PORT = 8000

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {
                "status": "OK"
            }
            self.wfile.write(json.dumps(status).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("Serving on port", PORT)
    httpd.serve_forever()
