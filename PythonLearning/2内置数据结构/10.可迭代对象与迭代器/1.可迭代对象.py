# -*- coding: utf-8 -*-
# @Time    : 2020/12/25 15:41
# @Author  : wanghc
# @File    : 1.可迭代对象.py
# @Software: PyCharm

r = range(10)

r.__iter__()

'''
可迭代对象都有这么一个方法，有__iter__的对象叫可迭代对象。

可迭代对象出现在for in 循环中，或者说for in 语句需要可迭代对象
'''

for x in range(10):
    pass