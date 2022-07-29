# OneText API

## 基本简介

&emsp;&emsp;灵感来源：[lz233/OneText-Library](https://github.com/lz233/OneText-Library)

&emsp;&emsp;请求地址：[https://onetext.cicada000.work/api](https://onetext.cicada000.work/api)

&emsp;&emsp;返回格式（与&emsp;[lz233/OneText-Library](https://github.com/lz233/OneText-Library)&emsp;稍有不同）：

```json
{
  "text": "句子内容",
  "raw": "如果句子是译文，可以在这里填写原文",
  "by": "句子的原作者",
  "from": "句子被收集的来源",
  "time": "句子被收集/创作的时间"
}
```

## 进阶用法

### 使用GET请求返回指定句子

&emsp;&emsp;在请求URL后加&emsp; /?category=XXX &emsp;返回XXX类型的句子，例如输入&emsp;[https://onetext.cicada000.work/?category=Anime](https://onetext.cicada000.work/?category=Anime)&emsp;则返回&emsp;[Anime.json](https://github.com/Cicada000/OneText-API-Python/blob/main/Anime.json)&emsp;中的句子，目前有**Anime**、**Poem**、**Other**三类。（参数不区分大小写）

### 使用Vercel一键部署

&emsp;&emsp;点击下方按钮根据提示操作即可

&emsp;&emsp;[![Powered by Vercel](https://www.datocms-assets.com/31049/1618983297-powered-by-vercel.svg)](https://vercel.com/new/clone?repository-url=https://github.com/Cicada000/OneText-API-Python)

&emsp;&emsp;关于修改项目具体参数，须在&emsp;[/api/index.py](https://github.com/Cicada000/OneText-API-Python/blob/main/api/index.py)&emsp;中修改，具体参考&emsp;[/api/README.md](https://github.com/Cicada000/OneText-API-Python/blob/main/api/README.md)


