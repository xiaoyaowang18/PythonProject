# -*- coding: utf-8 -*-
# @Time    : 2021/10/11 15:50
# @Author  : wanghc
# @File    : 5、终止进程.py
# @Software: PyCharm


import multiprocessing

import time

'''
终止进程不止有守护进程这一种做法，我们也可以通过 terminate 方法来终止某个子进程，
另外我们还可以通过 is_alive 方法判断进程是否还在运行。
'''


def process():
    print('Starting')

    time.sleep(5)

    print('Finished')


if __name__ == '__main__':
    p = multiprocessing.Process(target=process)

    print('Before:', p, p.is_alive())

    p.start()

    print('During:', p, p.is_alive())

    p.terminate()

    print('Terminate:', p, p.is_alive())

    p.join()

    print('Joined:', p, p.is_alive())
