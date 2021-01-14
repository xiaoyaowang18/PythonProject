# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 22:02
# @Author  : wanghc
# @File    : 2,进阶.py
# @Software: PyCharm

'''
Diango源码很多类都是__str__ __repr__的方法

为什么要写呢？
因为记录日志的时候，不可能把实例内存对象打印出来，没意义。

如果想看实例的关键属性
那么往往str和repr是一个方法
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point<{},{}>'.format(self.x, self.y)

    def __repr__(self):
        return 'Point({},{})'.format(self.x, self.y)

    __repr__ = __str__


p1 = Point(1, 2)
print(p1)

'''
总结：
可视化主要用在打log的时候
'''
