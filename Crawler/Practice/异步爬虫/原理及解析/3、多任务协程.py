# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 16:44
# @Author  : wanghc
# @File    : 3、多任务协程.py
# @Software: PyCharm

'''
可以定义一个 task 列表，然后使用 asyncio 的 wait 方法即可执行，实现多任务协程

for 循环创建了五个 task，组成了一个列表，然后把这个列表首先传递给了 asyncio 的 wait() 方法，
然后再将其注册到时间循环中，就可以发起五个任务了。
'''

import asyncio
import requests


async def request():
    url = 'https://www.baidu.com'
    response = requests.get(url)
    return response


tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('Tasks', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task Result:', task.result())
