# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 20:58
# @Author  : wanghc
# @File    : 3.线程的实现.py
# @Software: PyCharm


import threading


def work():
    print('work')


# 创建一个线程对象，target参数传入需要执行的逻辑
thread = threading.Thread(target=work)

# 启动线程  start方法启动一个线程，当这个线程的逻辑执行完毕后，线程自动退出
thread.start()

# 有没有什么方法来关闭线程？
'''
没有stop方法来关闭线程的，所以python没有主动退出线程的方法。
所以在写线程的时候一定要写他的退出条件，一定要注意线程的退出。

所以服务端的线程通常会做一个while true的循环
'''


def work2(x):
    print('work {}'.format(x))


for x in range(5):
    # *args* is the argument tuple for the target invocation. Defaults to ().  可传入参数
    t = threading.Thread(target=work2, args=(x,))
    t.start()
