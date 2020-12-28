# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 3.返回多个结果.py
@time: 2020/12/28 23:40
"""

'''
如果需要返回多个值怎么处理？

可以用到封装和解构
'''


def fn():
    return 3, 5


ret = fn()
print(type(ret))  # <class 'tuple'>
print(ret)  # (3, 5)

'''
可以看到结果是一个元组，当函数需要返回多个值的时候，可以把结果封装成元组。
'''

x, y = fn()
print(x,y)

'''
也可以通过解构来获取fn函数的所有返回值
'''

'''
有时候如果只是想结束函数，并不想返回值，可以return或return None
'''