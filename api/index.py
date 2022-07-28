from flask import Flask, request
import requests , json , random

def select(a):
    list = ["Anime","Poem","Other"]
    if str.title(str(a)) in list :
        return str.title(str(a))
    else :
        return random.choice(list)

app = Flask(__name__)

@app.route('/api',methods=["GET"])

def return_OneText():

    category = request.args.get("category")
    category = str(category)
    category = select(category)

    url = requests.get("https://onetext.cicada000.work/" + category + ".json")
    text = url.text
    OneTextRaw = json.loads(text)
    OneText = OneTextRaw[random.randint(0,(len(OneTextRaw)-1))]
    OneText = str(OneText)
    OneText = OneText.replace("\'","\"")

    return OneText, 200, {"Content-Type":"application/json"}
    