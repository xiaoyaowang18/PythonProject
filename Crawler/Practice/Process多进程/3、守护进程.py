# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 15:32
# @Author  : wanghc
# @File    : 3、守护进程.py
# @Software: PyCharm

from multiprocessing import Process

import time

'''
在多进程中，同样存在守护进程的概念，如果一个进程被设置为守护进程，当父进程结束后，子进程会自动被终止，
我们可以通过设置 daemon 属性来控制是否为守护进程。
'''


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

        p.daemon = True

        p.start()



print('Main Process ended')
