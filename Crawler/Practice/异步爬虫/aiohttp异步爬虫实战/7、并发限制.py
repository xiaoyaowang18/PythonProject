# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 7、并发限制.py
@time: 2021/10/13 22:06
"""

'''
由于 aiohttp 可以支持非常大的并发，比如上万、十万、百万都是能做到的，但这么大的并发量，目标网站是很可能在短时间内无法响应的，
而且很可能瞬时间将目标网站爬挂掉。所以我们需要控制一下爬取的并发量。
在一般情况下，我们可以借助于 asyncio 的 Semaphore 来控制并发量
'''

import asyncio
import aiohttp
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
CONCURRENCY = 5
URL = 'https://www.baidu.com'
semaphore = asyncio.Semaphore(CONCURRENCY)


async def scrape_api():
    async with semaphore:
        logging.info('scraping %s', URL)
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as response:
                await asyncio.sleep(1)
                return await response.text()


async def main():
    scrape_api_taks = [asyncio.ensure_future(scrape_api()) for _ in range(20)]
    await asyncio.gather(*scrape_api_taks)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
