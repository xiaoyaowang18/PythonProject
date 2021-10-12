# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 11:28
# @Author  : wanghc
# @File    : 4、互斥锁.py
# @Software: PyCharm


import threading

import time

'''
https://docs.python.org/zh-cn/3.7/library/threading.html#module-threading

某个线程在对数据进行操作前，需要先加锁，这样其他的线程发现被加锁了之后，就无法继续向下执行，会一直等待锁被释放，
只有加锁的线程把锁释放了，其他的线程才能继续加锁并对数据做修改，修改完了再释放锁。
这样可以确保同一时间只有一个线程操作数据，多个线程不会再并发或并行取和修改同一个数据，这样最后的运行结果就是对的了。
'''

count = 0


class MyThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count

        lock.acquire()

        temp = count + 1

        time.sleep(0.001)

        count = temp

        lock.release()


lock = threading.Lock()

threads = []

for _ in range(100):
    thread = MyThread()

    thread.start()

    threads.append(thread)

for thread in threads:
    thread.join()

print(f'Final count: {count}')
