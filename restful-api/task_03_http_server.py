#!/usr/bin/env python3
"""task_03_http_server.py: A simple HTTP server
that returns a JSON response."""

import json
import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """A simple HTTP request handler."""
    def do_GET(self):
        """Handle GET requests."""
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/info":
            self.send_response(200)  # HTTP status 200 OK
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self.wfile.write(json.dumps(data).encode("utf-8"))
        else:
            self.send_error(404, "Endpoint not found")


def run(server_class=HTTPServer,
        handler_class=SimpleHTTPRequestHandler, port=8000):
    """ Set up and run the HTTP server."""
    server_address = ("localhost", port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()


if __name__ == "__main__":
    run()  # Run the server
