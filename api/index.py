from flask import Flask , request , render_template
from PIL import Image , ImageDraw , ImageFont
import requests , json , random , base64

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
    

@app.route('/image')

def build():

    url = requests.get("https://onetext.cicada000.work/api")
    OneText = json.loads(url.text)
    Text = OneText['text']
    Time = OneText['time']
    Author = OneText['by']
    From = OneText['from']

    TextDict = Text.split("\n")
    MaxText = len(max(TextDict, key=len, default=''))
    Row = len(TextDict)

    # 判断长宽
    if 400 + 70*MaxText > 1000:
        TextLenth = 440 + 70*MaxText
    else:
        TextLenth = 1000

    if Row > 3:
        TextHeight = Row*90 + 560
    else:
        TextHeight = 800

    # 生成背景图片
    Background = Image.new('RGB' , (TextLenth  , TextHeight) , (255 , 255 , 255))

    # 在图片上绘制
    ImageDraw.Draw(Background).text((70 , 70) , "“" , font=ImageFont.truetype("api/LXGWWenKaiGBFusion-Bold.ttf", 300, encoding="unic") , fill=(180 , 180 , 180))
    ImageDraw.Draw(Background).text((220 , 200) , Text , font=ImageFont.truetype("api/LXGWWenKaiGBFusion-Bold.ttf", 70, encoding="unic") , spacing=20 , fill=(0 , 0 , 0))
    ImageDraw.Draw(Background).text((TextLenth - 180 , 70 + (Row + 2)*70) , "”" , font=ImageFont.truetype("api/LXGWWenKaiGBFusion-Bold.ttf", 300, encoding="unic") , fill=(180 , 180 , 180))
    ImageDraw.Draw(Background).text((TextLenth - 180 , TextHeight - 230) , "——" + Author , font=ImageFont.truetype("api/LXGWWenKaiGBFusion-Bold.ttf", 50, encoding="unic") , anchor="rd" , fill=(50 , 50 , 50))
    ImageDraw.Draw(Background).text((TextLenth - 180 , TextHeight - 160) , Time + From , font=ImageFont.truetype("api/LXGWWenKaiGBFusion-Bold.ttf", 30, encoding="unic") , anchor="rd" , fill=(30 , 30 , 30))
    ImageDraw.Draw(Background).rounded_rectangle((40 , 40 , TextLenth - 40 , TextHeight - 40) , 15 , width = 5 , outline=(227 , 227 , 227))

    # 图片转base64
    def image_to_base64(image):
        img = image
        output_buffer = BytesIO()
        img.save(output_buffer, format='PNG')
        byte_data = output_buffer.getvalue()
        base64_str = base64.b64encode(byte_data)
        return base64_str

    image_base64 = image_to_base64(Background).decode('UTF-8')
    return  render_template("index.html" , image_base64 = image_base64)
