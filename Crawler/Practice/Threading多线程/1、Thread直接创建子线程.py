# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 10:50
# @Author  : wanghc
# @File    : 1、Thread直接创建子线程.py
# @Software: PyCharm

import threading

import time

'''
使用 Thread 类来创建一个线程，创建时需要指定 target 参数为运行的方法名称，
如果被调用的方法需要传入额外的参数，则可以通过 Thread 的 args 参数来指定
'''


def target(second):
    print(f'Threading {threading.current_thread().name} is running')

    print(f'Threading {threading.current_thread().name} sleep {second}s')

    time.sleep(second)

    print(f'Threading {threading.current_thread().name} is ended')


print(f'Threading {threading.current_thread().name} is running')

for i in [1, 5]:
    thread = threading.Thread(target=target, args=[i])

    thread.start()

print(f'Threading {threading.current_thread().name} is ended')
