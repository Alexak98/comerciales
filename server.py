import http.server
import socketserver
import os

os.chdir("/Users/alexander/Desktop/Comerciales")
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 3000), handler) as httpd:
    print("Serving on port 3000")
    httpd.serve_forever()
