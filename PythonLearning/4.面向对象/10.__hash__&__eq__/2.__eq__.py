# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 20:29
# @Author  : wanghc
# @File    : 2.__eq__.py
# @Software: PyCharm

'''
通常__hash__会和__eq__一起使用，因为解释器通常同时判断hash是否相等以及实例是否相等。
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 判断hash值是否相等
    def __hash__(self):
        return hash('{}:{}'.format(self.x, self.y))

    # 判断实例是否相等
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(set([p1, p2]))  # {<__main__.Point object at 0x000001FCBAD12F60>}
