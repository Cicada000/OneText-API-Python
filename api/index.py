from http.server import BaseHTTPRequestHandler
import json , requests

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        url = requests.get("https://onetext-api.vercel.app/Data.json")
        text = url.text
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(text.encode())
        return