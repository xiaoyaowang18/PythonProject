# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 1.位置参数.py
@time: 2020/12/28 22:26
"""


# 1.位置参数
def add(x, y):
    ret = x + y
    print('{}+{}'.format(x, y))
    return ret


'''
位置参数就是按照他的位置来传入参数
比如这个add，add(3,5)和add(5,3)虽然结果一样，但实际调用的时候函数的运行是不一样的，变量的值也不一样。
'''
