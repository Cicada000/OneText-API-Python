from http.server import BaseHTTPRequestHandler
import json , requests , random

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        url = requests.get("https://onetext.cicada000.work/Data.json")
        text = url.text
        OneTextRaw = json.loads(text)
        OneText = OneTextRaw[random.randint(0,(len(OneTextRaw)-1))]
        OneText = str(OneText)
        OneText = OneText.replace("\'","\"")
        
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(OneText.encode())
        
        return
