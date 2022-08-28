from flask import Flask, request
import requests , json , random

def select(a):
    list = ["ACGN","POEM","OTHER"]
    if str.upper(str(a)) in list :
        return str.upper(str(a))
    else :
        return random.choice(list)

app = Flask(__name__)

@app.route('/',methods=["GET"])

def return_OneText():

    category = request.args.get("category")
    id = request.args.get("id")
    number = -1

    if id != None :
        id = id.split("-")
        category = id[0]
        id += '0'
        number = int(id[1])-1
    
    if category == None :
        category =  select(category)
    else :
        category = category.split()
        category = random.choice(category)
        category = select(category)

    url = requests.get("https://onetext.cicada000.work/" + category + ".json")
    text = url.text
    OneTextRaw = json.loads(text)

    if number == -1:
        number = random.randint(0,(len(OneTextRaw) - 1))
    else :
        number = number

    OneText = OneTextRaw[number]
    OneText = json.dumps(OneText , sort_keys = False , indent = 4 , separators = (',',':') , ensure_ascii = False)
 
    return OneText.encode(), 200, {"Content-Type":"application/json" , "Charset":"UTF-8"}
    
