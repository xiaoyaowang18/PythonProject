# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 3.惰性求值.py
@time: 2020/12/30 1:17
"""


# 写一个计数器

def counter():
    x = 0
    while True:
        x += 1
        yield x


c = counter()


def inc(c):
    return next(c)


print(inc(c))  # 1
print(inc(c))  # 2


# 可以封装的更好
def inc2():
    c = counter()
    return lambda: next(c)


ic = inc2()
print(ic())  # 1
print(ic())  # 2


# 最终版
# 对外不需要告诉别人inc是怎么样实现的，只需要让他知道每调用一次就会增加1
def inc3():
    def counter():
        x = 0
        while True:
            x += 1
            yield x

    c = counter()
    return lambda: next(c)


ic3 = inc3()
print(ic3())
print(ic3())
