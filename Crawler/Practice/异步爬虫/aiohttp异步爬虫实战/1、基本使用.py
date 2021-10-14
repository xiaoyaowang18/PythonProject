# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 1、基本使用.py
@time: 2021/10/13 21:34
"""

import aiohttp
import asyncio

'''
https://docs.aiohttp.org/en/stable/client_quickstart.html

1、除了必须要引入 aiohttp 这个库之外，还必须要引入 asyncio 这个库，因为要实现异步爬取需要启动协程，
而协程则需要借助于 asyncio 里面的事件循环来执行。除了事件循环，asyncio 里面也提供了很多基础的异步操作。

2、with as 语句用于声明一个上下文管理器，能够帮我们自动分配和释放资源，而在异步方法中，with as 前面加上 async 代表声明一个支持异步的上下文管理器。

3、对于一些返回 coroutine 的操作，前面需要加 await 来修饰，如 response 调用 text 方法，查询 API 可以发现其返回的是 coroutine 对象，
那么前面就要加 await；而对于状态码来说，其返回值就是一个数值类型，那么前面就不需要加 await。

4、事件循环就需要使用 asyncio 库，然后使用 run_until_complete 方法来运行。
'''


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(), response.status


async def main():
    async with aiohttp.ClientSession() as session:
        html, status = await fetch(session, 'https://cuiqingcai.com')
        print(f'html: {html[:100]}...')
        print(f'status: {status}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
