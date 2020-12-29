# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 4.应用.py
@time: 2020/12/30 1:29
"""

'''
斐波那契数列
'''


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 用递归的方式很简单，但是效率太低了

# 用生成器的方式
'''
递归转循环，解决递归问题 （应用一）
1.没有递归深度限制
2.递归的缺点都没有，因为他不用保存现场，这里的现场指函数。
'''


def fib2():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a


f = fib2()
print(next(f))
print(next(f))
print(next(f))
