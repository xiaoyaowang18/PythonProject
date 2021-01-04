# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 2.实现函数的类型检查.py
@time: 2021/1/5 7:15
"""
import inspect
import functools


def typejc(fn):
    @functools.wraps(fn)
    def wrap(*args, **kwargs):
        # 获取被装饰函数的所有参数
        parms = inspect.signature(fn).parameters

        # 检查关键字参数
        for k, v in kwargs.items():
            parm = parms[k]
            # parm.annotation != inspect._empty 排除没有加上类型注解的情况，不影响代码运行
            if parm.annotation != inspect._empty and not isinstance(v, parm.annotation):
                raise TypeError('parameter {} require {},but {}'.format(k, parms[k].annotation, type(k)))

        # 检查位置参数
        for i, arg in enumerate(args):
            parm = list(parms.values())[i]
            if parm.annotation != inspect._empty and not isinstance(arg, parm.annotation):
                raise TypeError('parameter {} require {},but {}'.format(parm.name, parm.annotation, type(arg)))

        return fn(*args, **kwargs)

    return wrap


@typejc
def add(x, y: int) -> int:
    return x + y


print(add(1, 1))
print(add(1, 'a'))
