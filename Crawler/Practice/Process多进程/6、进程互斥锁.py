# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 15:54
# @Author  : wanghc
# @File    : 6、进程互斥锁.py
# @Software: PyCharm

from multiprocessing import Process, Lock

import time

'''
实现了进程互斥，避免了多个进程同时抢占临界区（输出）资源。我们可以通过 multiprocessing 中的 Lock 来实现。
Lock，即锁，在一个进程输出时，加锁，其他进程等待。等此进程执行结束后，释放锁，其他进程可以进行输出。
'''


class MyProcess(Process):

    def __init__(self, loop, lock):

        Process.__init__(self)

        self.loop = loop

        self.lock = lock



    def run(self):

        for count in range(self.loop):

            time.sleep(0.1)

            # self.lock.acquire()

            print(f'Pid: {self.pid} LoopCount: {count}')

            # self.lock.release()



if __name__ == '__main__':

    lock = Lock()

    for i in range(10, 15):

        p = MyProcess(i, lock)

        p.start()
