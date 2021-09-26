# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: test.py.py
@time: 2021/9/23 6:51
"""

import asyncio

async def worker_1():
    print("work1")
    await asyncio.sleep(1)
    return 1

async def worker_2():
    print("work2")
    await asyncio.sleep(2)
    return 2 / 0

async def worker_3():
    print("work3")
    await asyncio.sleep(3)
    return 3

async def main():
    task_1 = asyncio.create_task(worker_1())
    task_2 = asyncio.create_task(worker_2())
    task_3 = asyncio.create_task(worker_3())

    print("哦哦哦")

    await asyncio.sleep(2)

    task_3.cancel()

    res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
    print(res)

asyncio.run(main())
