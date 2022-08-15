from flask import Flask, request
import requests , json , random

def select(a):
    list = ["ACGN","POEM","OTHER"]
    if str.upper(str(a)) in list :
        return str.upper(str(a))
    else :
        return random.choice(list)

app = Flask(__name__)

@app.route('/api',methods=["GET"])

def return_OneText():

    category = request.args.get("category")
    if category == None :
        category =  select(category)
    else :
        category = category.split()
        category = random.choice(category)
        category = select(category)

    url = requests.get("https://onetext.cicada000.work/" + category + ".json")
    text = url.text
    OneTextRaw = json.loads(text)
    OneText = OneTextRaw[random.randint(0,(len(OneTextRaw) - 1))]
    OneText = json.dumps(OneText , sort_keys = False , indent = 4 , separators = (',',':') , ensure_ascii = False)
 
    return OneText.encode(), 200, {"Content-Type":"application/json" , "Charset":"UTF-8"}
    
