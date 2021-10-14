# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 5、响应字段.py
@time: 2021/10/13 22:03
"""

import aiohttp
import asyncio


async def main():
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://httpbin.org/post', data=data) as response:
            print('status:', response.status)
            print('headers:', response.headers)
            print('body:', await response.text())
            print('bytes:', await response.read())
            print('json:', await response.json())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
