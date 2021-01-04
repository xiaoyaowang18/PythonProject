# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 1.inspect库.py
@time: 2021/1/5 7:06
"""

import inspect


def add(x: int, y: int) -> int:
    return x + y


sig = inspect.signature(add)

print(sig.parameters)  # 参数字典  OrderedDict([('x', <Parameter "x: int">), ('y', <Parameter "y: int">)])

print(sig.parameters.values())

print(sig.parameters['x'])  # 获取到x参数的信息，包括类型

parm = sig.parameters['x']
print(parm.default)  # 查看参数x的默认参数，如果有的话  <class 'inspect._empty'>

print(parm.annotation) # 查看x参数的类型  <class 'int'>



