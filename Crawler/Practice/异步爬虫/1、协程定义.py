# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 15:39
# @Author  : wanghc
# @File    : 1、协程定义.py
# @Software: PyCharm

'''
协程，英文叫作 Coroutine，又称微线程、纤程，协程是一种用户态的轻量级线程。

协程拥有自己的寄存器上下文和栈。协程调度切换时，将寄存器上下文和栈保存到其他地方，在切回来的时候，
恢复先前保存的寄存器上下文和栈。因此协程能保留上一次调用时的状态，即所有局部状态的一个特定组合，
每次过程重入时，就相当于进入上一次调用的状态。

协程本质上是个单进程，协程相对于多进程来说，无需线程上下文切换的开销，无需原子操作锁定及同步的开销，
编程模型也非常简单。

我们可以使用协程来实现异步操作，比如在网络爬虫场景下，我们发出一个请求之后，需要等待一定的时间才能得到响应，
但其实在这个等待过程中，程序可以干许多其他的事情，等到响应得到之后才切换回来继续处理，
这样可以充分利用 CPU 和其他资源，这就是协程的优势。
'''

'''
event_loop：事件循环，相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足条件发生的时候，就会调用对应的处理方法。

coroutine：中文翻译叫协程，在 Python 中常指代为协程对象类型，我们可以将协程对象注册到时间循环中，它会被事件循环调用。
我们可以使用 async 关键字来定义一个方法，这个方法在调用时不会立即被执行，而是返回一个协程对象。

task：任务，它是对协程对象的进一步封装，包含了任务的各个状态。

future：代表将来执行或没有执行的任务的结果，实际上和 task 没有本质区别。

另外我们还需要了解 async/await 关键字，它是从 Python 3.5 才出现的，专门用于定义协程。其中，async 定义一个协程，await 用来挂起阻塞方法的执行。
'''
import asyncio

'''
async定义的方法会变成一个无法直接执行的coroutine对象，必须注册到事件循环中才可以执行
'''


async def execute(x):
    print('Number:', x)


coroutine = execute(1)  # 返回一个协程对象
print('Coroutine:', coroutine)
print('After calling execute')
loop = asyncio.get_event_loop()  # 创建一个事件循环
loop.run_until_complete(coroutine)  # 将协程对象注册到事件循环中,实际上它进行了一个操作就是将 coroutine 封装成了 task 对象
print('After calling loop')

'''
把协程对象封装成task也可以进行显式申明
task = loop.create_task(coroutine)
loop.run_until_complete(task)

还可以直接通过 asyncio 的 ensure_future 方法
task = asyncio.ensure_future(coroutine)
'''
