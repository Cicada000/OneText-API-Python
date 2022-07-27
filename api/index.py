from http.server import BaseHTTPRequestHandler
import json , requests , random

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        url = requests.get("https://onetext.cicada000.work/Data.json")
        text = url.text
        OneTextRaw = json.loads(text,encoding="UTF-8")
        OneText = OneTextRaw[random.randint(0,(len(OneTextRaw)-1))]
        
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(OneTextRaw.encode('utf-8'))
        
        return
