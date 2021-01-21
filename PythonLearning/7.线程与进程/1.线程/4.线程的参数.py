# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 21:17
# @Author  : wanghc
# @File    : 4.线程的参数.py
# @Software: PyCharm

import threading

# 标识一个线程
print(threading.current_thread())


def work():
    print('work')


t = threading.Thread(target=work)
print(t.name)  # 线程的名字
print(t.ident)  # 线程的id
print(t.is_alive())  # 当前线程是否是活着的
