# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 3.带参数的装饰器.py
@time: 2021/1/4 21:35
"""

import datetime
import time
import functools

'''
假如现在要记录大于1秒的时间，并且对这个1秒单位作控制，通过参数传递进来
定义一个有参数的装饰器
'''


def _log(s):
    def logger(fn):
        @functools.wraps(fn)
        def wrag(*args, **kwargs):
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            end = datetime.datetime.now()
            if (end - start).total_seconds() > s:
                print('{} call took {}'.format(fn.__name__, end - start))
            return ret

        return wrag

    return logger


@_log(2)
def sleep(x):
    time.sleep(x)


sleep(2)  # sleep call took 0:00:02.009831
print(sleep.__name__)

'''
带参数的装饰器：一个函数，返回一个不带参数的装饰器。

装饰器只能传一个函数作为它的参数，不能传别的，如果要加参数，只能在外面再包一层。
'''
