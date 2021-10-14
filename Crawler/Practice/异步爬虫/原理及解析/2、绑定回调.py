# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 16:21
# @Author  : wanghc
# @File    : 2、绑定回调.py
# @Software: PyCharm

import asyncio
import requests


async def request():
    url = 'https://static1.scrape.center'
    response = requests.get(url)
    return response


def callback(task):
    print('Status:', task.result())


coroutine = request()
task = asyncio.ensure_future(coroutine)
'''
 callback 方法传递给了封装好的 task 对象，这样当 task 执行完毕之后就可以调用 callback 方法了，
 同时 task 对象还会作为参数传递给 callback 方法，调用 task 对象的 result 方法就可以获取返回结果了。
'''
task.add_done_callback(callback)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)

'''
实际上不用回调方法，直接在 task 运行完毕之后也可以直接调用 result 方法获取结果
'''