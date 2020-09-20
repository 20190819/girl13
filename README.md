# 一个针对某网站上图片的爬取工具，具有以下功能和特性:
* 使用 python 协程异步爬虫和下载图片
* 将爬取到的图片下载到本地指定文件夹
* 多次运行工程能够检测图片文件是否已经存在，如存在则不再重复下载

# 快速使用：
```bash

git clone git@github.com:yangliang4488/girl13.git

pip install asyncio 
pip install aiohttp 
pip install aiofiles 

python girl13.py

```