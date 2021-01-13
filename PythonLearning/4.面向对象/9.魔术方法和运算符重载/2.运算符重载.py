# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 23:09
# @Author  : wanghc
# @File    : 2.运算符重载.py
# @Software: PyCharm


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 重载了运算符加号的逻辑
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(1, 2)
p2 = Point(2, 3)
# print(p1 + p2)  如果直接相加是不行的
