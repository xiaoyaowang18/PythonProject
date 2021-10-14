# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 6、超时设置.py
@time: 2021/10/13 22:04
"""

import aiohttp
import asyncio

'''
如果超时的话，会抛出 TimeoutError 异常，其类型为 asyncio.TimeoutError，我们再进行异常捕获即可。
'''


async def main():
    timeout = aiohttp.ClientTimeout(total=1)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get('https://httpbin.org/get') as response:
            print('status:', response.status)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
