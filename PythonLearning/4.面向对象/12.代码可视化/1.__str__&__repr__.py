# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 21:47
# @Author  : wanghc
# @File    : 1.__str__&__repr__.py
# @Software: PyCharm

'''
假设我们有一个二维平面的点类
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point<{}.{}>'.format(self.x, self.y)

    def __repr__(self):
        return 'Point({}.{})'.format(self.x, self.y)


print(Point(1, 2))  # <__main__.Point object at 0x000001E0DFDA0EB8>

'''
打印的对象信息量并不多。如果打印出点的x,y值会更好，对代码调试很有帮助。
重写__str__方法后，打印
'''

print('{!s}'.format(Point(2, 3)))  # 支持后面的对象变成字符串

print('{!r}'.format(Point(1, 4)))  # 支持后面的对象变成字符串

'''
两个区别：
str在打印的时候，字符串格式化都默认打印出来的，所以通常是给人读的。
repr是给机器读的。
通常会重写str
'''
