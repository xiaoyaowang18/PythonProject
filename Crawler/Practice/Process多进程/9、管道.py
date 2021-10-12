# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 17:03
# @Author  : wanghc
# @File    : 9.py
# @Software: PyCharm

'''
刚才我们使用 Queue 实现了进程间的数据共享，那么进程之间直接通信，如收发信息，用什么比较好呢？可以用 Pipe，管道。

管道，我们可以把它理解为两个进程之间通信的通道。管道可以是单向的，即 half-duplex：一个进程负责发消息，另一个进程负责收消息；也可以是双向的 duplex，即互相收发消息。

默认声明 Pipe 对象是双向管道，如果要创建单向管道，可以在初始化的时候传入 deplex 参数为 False。
'''

from multiprocessing import Process, Pipe


class Consumer(Process):

    def __init__(self, pipe):
        Process.__init__(self)

        self.pipe = pipe

    def run(self):
        self.pipe.send('Consumer Words')

        print(f'Consumer Received: {self.pipe.recv()}')


class Producer(Process):

    def __init__(self, pipe):
        Process.__init__(self)

        self.pipe = pipe

    def run(self):
        print(f'Producer Received: {self.pipe.recv()}')

        self.pipe.send('Producer Words')


if __name__ == '__main__':
    pipe = Pipe()

    p = Producer(pipe[0])

    c = Consumer(pipe[1])

    p.daemon = c.daemon = True

    p.start()

    c.start()

    p.join()

    c.join()

    print('Main Process Ended')
