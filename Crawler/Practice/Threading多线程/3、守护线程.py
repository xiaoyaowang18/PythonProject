# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 11:24
# @Author  : wanghc
# @File    : 3、守护线程.py
# @Software: PyCharm

import threading

import time

'''
在线程中有一个叫作守护线程的概念，如果一个线程被设置为守护线程，那么意味着这个线程是“不重要”的，
这意味着，如果主线程结束了而该守护线程还没有运行完，那么它将会被强制结束。
在 Python 中我们可以通过 setDaemon 方法来将某个线程设置为守护线程。
'''


def target(second):
    print(f'Threading {threading.current_thread().name} is running')

    print(f'Threading {threading.current_thread().name} sleep {second}s')

    time.sleep(second)

    print(f'Threading {threading.current_thread().name} is ended')


print(f'Threading {threading.current_thread().name} is running')

t1 = threading.Thread(target=target, args=[2])

t1.start()

t2 = threading.Thread(target=target, args=[5])

t2.setDaemon(True)

t2.start()

print(f'Threading {threading.current_thread().name} is ended')
