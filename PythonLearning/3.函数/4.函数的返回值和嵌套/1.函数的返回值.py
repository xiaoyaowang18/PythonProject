# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 1.函数的返回值.py
@time: 2020/12/28 23:21
"""

'''调用add函数，发现没有打印，说明return语句除了返回值之外，还会结束函数，return之后的语句将不会被执行。'''


def add(x, y):
    return x + y
    print('打印呀')


add(1, 2)

'''
一个函数可以有多个return语句，执行到哪个return，就由哪个return返回结果并结束函数。
'''


def guess(x):
    if x > 3:
        return '>3'
    return '<= 3'


'''
假如函数fn，输入参数10，那么当i= 4的时候，就return结果并结束函数了。else语句并不会执行，因为for循环必须走完才会执行else,而现在中途就停止了。
所以return还有提前终止循环的能力，类似于break提前终止本层循环。
'''


def fn(x):
    for i in range(x):
        if i > 3:
            return i
    else:
        print('not bigger than 3')
