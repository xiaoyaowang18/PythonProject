# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 10:52
# @Author  : wanghc
# @File    : 2、继承Thread类创建子线程.py
# @Software: PyCharm

import threading

import time

'''
通过继承 Thread 类的方式创建一个线程，该线程需要执行的方法写在类的 run 方法里面即可
'''


class MyThread(threading.Thread):

    def __init__(self, second):
        threading.Thread.__init__(self)

        self.second = second

    def run(self):
        print(f'Threading {threading.current_thread().name} is running')

        print(f'Threading {threading.current_thread().name} sleep {self.second}s')

        time.sleep(self.second)

        print(f'Threading {threading.current_thread().name} is ended')


print(f'Threading {threading.current_thread().name} is running')

threads = []

for i in [1, 5]:
    thread = MyThread(i)

    threads.append(thread)

    thread.start()

'''
我们想要主线程等待子线程运行完毕之后才退出，可以让每个子线程对象都调用下 join 方法
'''
for thread in threads:
    thread.join()
print(f'Threading {threading.current_thread().name} is ended')
