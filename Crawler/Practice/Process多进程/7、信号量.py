# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 15:57
# @Author  : wanghc
# @File    : 7、信号量.py
# @Software: PyCharm

from multiprocessing import Process, Semaphore, Lock, Queue

import time

'''
信号量可以控制临界资源的数量，允许多个进程来访问共享资源，同时还需要限制能访问共享资源的进程的数量。
用 multiprocessing 库中的 Semaphore 来实现信号量。
'''


buffer = Queue(10)  # 共享队列

empty = Semaphore(2)  # 信号量、代表缓冲区空余数

full = Semaphore(0)   # 信号量、代表缓冲区占用数

lock = Lock()



class Consumer(Process):

    def run(self):

        global buffer, empty, full, lock

        while True:

            full.acquire()

            lock.acquire()

            buffer.get()

            print('Consumer pop an element')

            time.sleep(1)

            lock.release()

            empty.release()



class Producer(Process):

    def run(self):

        global buffer, empty, full, lock

        while True:

            empty.acquire()  # 1、占用一个缓冲区位置，缓冲区空闲区大小减1

            lock.acquire()   # 2、加锁

            buffer.put(1)    # 3、缓冲区进行操作

            print('Producer append an element')

            time.sleep(1)

            lock.release()  # 4、释放锁

            full.release()  # 5、占用的缓冲区位置数量加 1



if __name__ == '__main__':
    '''
    两个进程在交替运行，生产者先放入缓冲区物品，然后消费者取出，不停地进行循环。
    '''

    p = Producer()

    c = Consumer()

    p.daemon = c.daemon = True

    p.start()

    c.start()

    p.join()

    c.join()

    print('Main Process Ended')
