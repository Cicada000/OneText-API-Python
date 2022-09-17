# 关于API的详细说明

## 句子类别的添加和修改

&emsp;&emsp;众所周知，这个项目可以通过GET请求来获取各个类别的句子。开头的**select函数**就是用于判断获取到的GET参数是否为指定类型中的一种并格式化参数为符合的格式（这就是对GET参数大小写没有要求的原因）。如果要添加新的类别，直接在**select函数中的list列表**中添加即可，相应的，需要在根目录添加名称与列表元素相一致的JSON文件。

```python

def select(a):
    list = ["ACGN","POEM","OTHER","LYRICS"] #各个类别
    if str.upper(str(a)) in list : #判断GET参数是否在列表中
        return str.upper(str(a)) #返回GET参数，全部大写
    else :
        return random.choice(list) #随机返回列表元素

```

## JSON的格式化修改

&emsp;&emsp;一般情况下，你看到的返回的JSON格式应该是这样：

```json

{
    "text":"逸一时，误一世，逸久逸久罢矣龄。",
    "by":"田所浩二",
    "from":"《真夏の夜の淫梦》",
    "time":"1919.8.10",
    "id":"OTHER-1"
}

```
&emsp;&emsp;如果你想让它像下面这样显示或改变其他显示样式 &emsp; ~~虽然我觉得没人会想这么干~~：

```json

{"text":"逸一时，误一世，逸久逸久罢矣龄。","by":"田所浩二","from":"《真夏の夜の淫梦》","time":"1919.8.10","id":"OTHER-1"}

```

&emsp;&emsp;你可以将**json.dumps**函数内的参数进行修改，具体见下：

```python

OneText = json.dumps(OneText , 
                    sort_keys = False , #是否按字母排序
                    indent = 4 ,  #开头空格数
                    separators = (',',':') ,  #遇到','换行，删去该参数即可返回上方JSON格式
                    ensure_ascii = False) #字符编码，删去该参数中文采用Unicode编码

```

## 最后值得注意的一点

&emsp;&emsp;别忘了把获取JSON的域名改成部署你项目的域名。

```python

url = requests.get("https://onetext.cicada000.work/" + category + ".json") #没错就是这里

```
