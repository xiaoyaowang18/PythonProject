# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 17:06
# @Author  : wanghc
# @File    : 4、协程实现.py
# @Software: PyCharm

'''
实现异步处理，我们得先有挂起的操作，当一个任务需要等待IO结果的时候，可以挂起当前任务，
转而去执行其他任务，这样才能充分利用好资源。

要实现异步，需要了解一下await的用法，使用await可以将耗时等待的操作挂起，让出控制权。
当协程执行的时候遇到await，时间循环就会将本协程挂起，转而去执行其他的协程，直到其他的协程挂起或执行完毕。

根据官方文档说明，await 后面的对象必须是如下格式之一：

A native coroutine object returned from a native coroutine function，一个原生 coroutine 对象。

A generator-based coroutine object returned from a function decorated with types.coroutine，
一个由 types.coroutine 修饰的生成器，这个生成器可以返回 coroutine 对象。

An object with an __await__ method returning an iterator，一个包含 __await__ 方法的对象返回的一个迭代器。

可以参见：https://www.python.org/dev/peps/pep-0492/#await-expression。

aiohttp 是一个支持异步请求的库，利用它和 asyncio 配合我们可以非常方便地实现异步请求操作。
'''

import asyncio
import requests
import time
import logging
import aiohttp

'''
这个 get 方法第一步的执行是非阻塞的，挂起之后立马被唤醒，所以立即又进入执行，创建了 ClientSession 对象，
接着遇到了第二个 await，调用了 session.get 请求方法，然后就被挂起了，由于请求需要耗时很久，所以一直没有被唤醒。

当第一个 task 被挂起了，那接下来该怎么办呢？事件循环会寻找当前未被挂起的协程继续执行，于是就转而执行第二个 task 了，
也是一样的流程操作，直到执行了第十个 task 的 session.get 方法之后，全部的 task 都被挂起了。
所有 task 都已经处于挂起状态，怎么办？只好等待了。5 秒之后，几个请求几乎同时都有了响应，然后几个 task 也被唤醒接着执行。

这就是异步操作的便捷之处，当遇到阻塞式操作时，任务被挂起，程序接着去执行其他的任务，而不是傻傻地等待，
这样可以充分利用 CPU 时间，而不必把时间浪费在等待 IO 上。
'''

start = time.time()


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    await response.text()
    await session.close()
    return response


async def request():
    url = 'https://static4.scrape.center/'
    print('waiting for', url)
    response = await get(url)  # coroutine 对象
    print('get response from', url, 'response', response)


tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)
