# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 4、POST数据.py
@time: 2021/10/13 21:59
"""
import aiohttp
import asyncio

'''
其对应的请求头的 Content-type 为 application/x-www-form-urlencoded
'''


async def main():
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://httpbin.org/post', data=data) as response:
            print(await response.text())


'''
其对应的请求头的 Content-type 为 application/json,将 post 方法的 data 参数改成 json 即可
'''


async def main2():
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://httpbin.org/post', json=data) as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
