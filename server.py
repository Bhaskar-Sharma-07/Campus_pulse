#!/usr/bin/env python3
"""
Campus Pulse - Local Web Server
Runs a lightweight HTTP server and opens Campus Pulse in your default browser.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 5173
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and caching headers for smooth local evaluation
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

def run():
    os.chdir(DIRECTORY)
    server_address = ('', PORT)
    
    # Try preferred port, or fall back to port 0 (dynamic free port)
    try:
        httpd = socketserver.TCPServer(server_address, Handler)
        port_used = PORT
    except OSError:
        httpd = socketserver.TCPServer(('', 0), Handler)
        port_used = httpd.server_address[1]

    url = f"http://localhost:{port_used}/index.html"
    print("\n" + "="*60)
    print("  ⚡ Campus Pulse — College Hackathon Web App")
    print(f"  🌐 Running locally at: {url}")
    print("  👉 Opening in default browser...")
    print("  Press Ctrl+C to stop the server.")
    print("="*60 + "\n")

    webbrowser.open(url)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[Campus Pulse] Server gracefully stopped.")
        sys.exit(0)

if __name__ == '__main__':
    run()
