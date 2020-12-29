# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 1.定义.py
@time: 2020/12/30 0:50
"""


# 生成器其实也是一个函数
def g():
    for x in range(10):
        yield x


f = g()
print(f)  # <generator object g at 0x000001582B860270>

print(next(f))  # 0
print(next(f))  # 1

'''
有__iter__方法，是一个可迭代对象
有__next__方法，是一个迭代器
有yield关键字，是迭代器中特殊的内容，叫生成器
执行一次f = g(),根据函数的执行流程，现场应该已经被销毁了，但是到后面发现f还是有值，说明还可以继续调用next
事实上，函数的现场没有被销毁，这是生成器函数和普通函数不太一样的地方。
'''




