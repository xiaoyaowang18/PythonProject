# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 15:41
# @Author  : wanghc
# @File    : 4、进程等待.py
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

    processes = []
    for i in range(2, 5):
        p = MyProcess(i)
        processes.append(p)
        p.daemon = True
        p.start()
    for p in processes:
        p.join()  # 让所有子进程都执行完了然后再结束
        # p.join(1)  # 传入 1，代表最长等待 1 秒

'''
默认情况下，join 是无限期的。也就是说，如果有子进程没有运行完毕，主进程会一直等待。
这种情况下，如果子进程出现问题陷入了死循环，主进程也会无限等待下去。怎么解决这个问题呢？
可以给 join 方法传递一个超时参数，代表最长等待秒数。
如果子进程没有在这个指定秒数之内完成，会被强制返回，主进程不再会等待。也就是说这个参数设置了主进程等待该子进程的最长时间。
'''
