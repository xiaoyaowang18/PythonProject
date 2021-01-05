# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 1.cache装饰器.py
@time: 2021/1/5 21:29
"""

'''
写一个cache装饰器，允许过期。
当某个函数被cache装饰器装饰过后，在过期时间内重复调用它，是返回的缓存结果，而不是重新计算。

cache的必要元素：Key -> value

key是我们的参数，value是我们的返回值
'''
import functools
import datetime
import inspect


def cache(expire=0):
    def _cache(fn):
        cache = {}

        @functools.wraps(fn)
        def wrap(*args, **kwargs):

            key = []

            # 获取函数的参数字典
            parms = inspect.signature(fn).parameters

            # 处理位置参数
            for i, arg in enumerate(args):  # args传入进来只有参数的值，所以要先获取参数名
                # 得到参数字典中的key
                name = list(parms.keys())[i]
                key.append((name, arg))  # [('x',1),('y',5)]

            # key.extend(kwargs.items())
            # 处理关键字参数

            for k, v in kwargs.items():
                key.append((k, v))

            # 要怎么拼接？先做一个排序
            key.sort(key=lambda x: x[0])

            # 做一个列表解析，解析完做一个Json
            key = '&'.join(['{}={}'.format(name, arg) for name, arg in key])

            print(key)  # 'x=1&y=5'

            if key in cache.keys():
                ret, timestamp = cache[key]
                # 超时检测
                if expire == 0 or datetime.datetime.now().timestamp() - timestamp < expire:
                    print('cache hit')
                    return ret

            ret = fn(*args, **kwargs)
            print('cache miss')

            cache[key] = (ret, datetime.datetime.now().timestamp())
            return ret

        return wrap

    return _cache


@cache(expire=1609869255)
def add(x, y):
    return x + y


add(1, 5)
add(1, 5)  # 第二次命中缓存
