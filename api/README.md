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

## 值得注意的一点

&emsp;&emsp;别忘了把获取JSON的域名改成部署你项目的域名。

```python

url = requests.get("https://onetext.cicada000.work/" + category + ".json") #没错就是这里

```
