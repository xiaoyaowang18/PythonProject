# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 15:26
# @Author  : wanghc
# @File    : 2、继承Process类.py
# @Software: PyCharm

from multiprocessing import Process

import time


class MyProcess(Process):

    def __init__(self, loop):
        Process.__init__(self)

        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)

            print(f'Pid: {self.pid} LoopCount: {count}')


if __name__ == '__main__':

    for i in range(2, 5):
        p = MyProcess(i)

        p.start()
