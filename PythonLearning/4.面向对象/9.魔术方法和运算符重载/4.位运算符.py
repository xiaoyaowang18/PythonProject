# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 23:20
# @Author  : wanghc
# @File    : 4.位运算符.py
# @Software: PyCharm


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __and__(self, other):
        return self.x & other.x, self.y & other.y

    def __or__(self, other):
        return self.x | other.y, self.y | other.y


p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1 & p2)
print(p1 | p2)
