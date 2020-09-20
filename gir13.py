import aiohttp
import aiofiles
import asyncio
import re
from lxml import etree
import time
import os
import hashlib
import time
import sys

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}


def md5Name(url):
    res = re.findall(r"http://149.129.105.250/(.*?)\.(\w+)$", url)[0]
    name = res[0]
    suffix = res[1]
    md5 = hashlib.md5()
    md5.update(name.encode('utf-8'))
    return './girl13/{}.{}'.format(md5.hexdigest(), suffix)


async def getHtml(url):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url, headers=headers) as response:
            html = await response.text()
            # 手动挂起
            await parseHtml(html)


async def parseHtml(html_text):
    tree = etree.HTML(html_text)
    img_urls = tree.xpath(
        "//div[contains(@class,'entry-content')]/a/p/img/@src")
    for item in img_urls:
        await downImage(item)


async def downImage(url):
    file_name = md5Name(url)
    if(not os.path.exists(file_name)):
        print('开始下载图片...', file_name)
        async with aiohttp.ClientSession() as session:
            async with await session.get(url, headers=headers) as response:
                source = await response.read()
                async with aiofiles.open(file_name, 'wb') as fp:
                    await fp.write(source)
                    print('下载图片完成')
    else:
        print('图片已存在')

if __name__ == "__main__":
    print("爬取开始...")
    start = time.time()
    tasks = [asyncio.ensure_future(
        getHtml('http://www.girl13.com/page/{}/'.format(i))) for i in range(1, 607)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print("爬取完成,耗时：", time.time()-start)
