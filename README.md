# OneText API

![Deployments](https://img.shields.io/github/deployments/Cicada000/OneText-API-Python/Production?logo=Vercel&style=for-the-badge)

## 基本简介

&emsp;&emsp;灵感来源：[lz233/OneText-Library](https://github.com/lz233/OneText-Library)

&emsp;&emsp;请求地址：[https://onetext.cicada000.work](https://onetext.cicada000.work)

&emsp;&emsp;返回格式（与[lz233/OneText-Library](https://github.com/lz233/OneText-Library)稍有不同）：

```json
{
  "text": "句子内容",
  "raw": "如果句子是译文，可以在这里填写原文",
  "by": "句子的原作者",
  "from": "句子被收集的来源",
  "time": "句子被收集/创作的时间",
  "id": "句子id，格式为 类别-序号"
}
```

## 进阶用法

### 使用GET请求返回指定句子

### &emsp;&emsp;**参数category**

&emsp;&emsp;在请求URL后加 **?category=XXX** 返回XXX类型的句子，例如输入[https://onetext.cicada000.work?category=ACGN](https://onetext.cicada000.work?category=ACGN)则返回[ACGN.json](https://github.com/Cicada000/OneText-API-Python/blob/main/ACGN.json)中的句子，目前有**ACGN**、**POEM**、**OTHER**、**LYRICS**四类。（参数不区分大小写）

&emsp;&emsp;如果你想获取多个类别中的句子，可以使用 + 分隔类别，例如输入[https://onetext.cicada000.work?category=ACGN+POEM](https://onetext.cicada000.work?category=ACGN+POEM)则会返回[ACGN.json](https://github.com/Cicada000/OneText-API-Python/blob/main/ACGN.json)[POEM.json](https://github.com/Cicada000/OneText-API-Python/blob/main/POEM.json)中其中一类的句子。

&emsp;&emsp;值得注意的是，如果GET请求的参数填写错误，还是会返回所有类别的句子。

### &emsp;&emsp;**参数id**

&emsp;&emsp;在请求URL后加 ?id=xxxx-x 返回xxxx类型中的第x条句子（具体id可见json文件中每个句子的id参数），例如输入[https://onetext.cicada000.work?id=other-3](https://onetext.cicada000.work?id=other-3)则返回[OTHER.json](https://github.com/Cicada000/OneText-API-Python/blob/main/OTHER.json)中的第三条句子。

&emsp;&emsp;值得注意的是，当id参数和category参数同时出现在GET请求中时，会优先使用id参数。

### 使用Vercel一键部署

&emsp;&emsp;点击下方按钮根据提示操作即可

&emsp;&emsp;[![Powered by Vercel](https://www.datocms-assets.com/31049/1618983297-powered-by-vercel.svg)](https://vercel.com/new/clone?repository-url=https://github.com/Cicada000/OneText-API-Python)

&emsp;&emsp;关于修改项目具体参数，须在[/index.py](https://github.com/Cicada000/OneText-API-Python/blob/main/api/index.py)中修改，具体参考[/README.md](https://github.com/Cicada000/OneText-API-Python/blob/main/README.md)

## TODO

返回图片格式一言，详见[Onetext-Image](https://github.com/Cicada000/Onetext-Image)
