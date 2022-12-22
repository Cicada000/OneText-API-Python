from flask import Flask , request , jsonify
import requests , json , random

def select(a):
    list = ["ACGN","POEM","OTHER","LYRICS"]
    if str.upper(str(a)) in list :
        return str.upper(str(a))
    else :
        return random.choice(list)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

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
 
    return jsonify(OneText)
