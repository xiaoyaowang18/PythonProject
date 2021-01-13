# -*- coding: utf-8 -*-
# @Time    : 2021/1/13 23:17
# @Author  : wanghc
# @File    : 3.算术运算符.py
# @Software: PyCharm

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 重载了运算符加号的逻辑
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

# 可以通过int里的方法找到大多数运算符对应的方法。
print(help(int))