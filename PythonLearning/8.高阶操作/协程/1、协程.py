# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 1、协程.py
@time: 2021/9.测试/17 22:09
"""

'''
1、以爬虫为例，爬取的操作并发化
'''
import asyncio

'''
async 修饰词声明异步函数
await 执行协程，程序会堵塞在这里，进入被调用的协程函数，执行完毕后返回再继续
asyncio.run 来触发运行
'''

async def crawl_page(url):
    print("crawling {}".format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)         # 在这里休息若干秒，挂起当前任务，以允许其他任务运行
    print("ok {}".format(url))


async def main(urls):
    for url in urls:
        await crawl_page(url)


# asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))

'''
通过 asyncio.create_task 来创建任务
任务创建后很快被调度执行，这样我们的代码不会阻塞在任务这里，所以我们要等所有任务跑完
运行总时长等于运行时间最长的爬虫。
'''


async def main2(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    #  写法1 ：
    # for task in tasks:
    #   await task
    await asyncio.gather(*tasks)


# asyncio.run(main2(['url_1', 'url_2', 'url_3', 'url_4']))


'''
2、解密协程运行时
'''


async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)  # 4、await asyncio.sleep(1)  从当前任务切出，事件调度器开始调度worker_2
    print('worker_1 done')  # 6、一秒钟后，worker_1 的 sleep 完成，事件调度器将控制权重新传给 task_1，输出 'worker_1 done'，task_1 完成任务，从事件循环中退出


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)  # 5、await asyncio.sleep(1)  从当前任务切出，事件调度器从这个时候开始暂停调度；
    print('worker_2 done')  # 8、两秒钟后，worker_2 的 sleep 完成，事件调度器将控制权重新传给 task_2，输出 'worker_2 done'，task_2 完成任务，从事件循环中退出；


async def main():
    task1 = asyncio.create_task(worker_1())  # 2、task1、task2被创建，并进入事件循环等待
    task2 = asyncio.create_task(worker_2())
    print('before await')
    await task1             # 3、await task1执行，用户选择从当前的主任务中切出，事件调度器开始调度worker_1
    print('awaited worker_1')  # 7、await task1完成，事件调度器将控制器传给主任务，输出 'awaited worker_1'，·然后在 await task2 处继续等待；
    await task2
    print('awaited worker_2')  # 9.测试、主任务输出 'awaited worker_2'，协程全任务结束，事件循环结束


# asyncio.run(main())  # 1、进入main函数，事件循环开启
'''
输出结果
before await
worker_1 start
worker_2 start
worker_1 done
awaited worker_1
worker_2 done
awaited worker_2
'''

'''
3、给某些协程任务限定运行时间，超时即取消，某些协程任务出现错误该如何处理
'''


async def work1():
    await asyncio.sleep(1)
    return 1


async def work2():
    await asyncio.sleep(2)
    return 2 / 0


async def work3():
    await asyncio.sleep(3)
    return 3


async def main():
    task1 = asyncio.create_task(work1())
    task2 = asyncio.create_task(work2())
    task3 = asyncio.create_task(work3())

    await asyncio.sleep(2)
    task3.cancel()

    res = await asyncio.gather(task1, task2, task3, return_exceptions=True)  # 要注意return_exceptions=True这行代码。如果不设置这个参数，错误就会完整地 throw 到我们这个执行层，从而需要 try except 来捕捉，这也就意味着其他还没被执行的任务会被全部取消掉。为了避免这个局面，我们将 return_exceptions 设置为 True 即可。
    print(res)

asyncio.run(main())