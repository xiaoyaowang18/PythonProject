# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 2、URL参数设置.py
@time: 2021/10/13 21:49
"""

import aiohttp
import asyncio


async def main():
    params = {'name': 'germy', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/get', params=params) as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
