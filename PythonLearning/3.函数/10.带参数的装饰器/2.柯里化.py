# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 16:17
# @Author  : wanghc
# @File    : 2.柯里化.py
# @Software: PyCharm


import datetime
import time
import functools

'''
柯里化：其实是数学上的概念，目的是让多个参数变成单个参数
'''


# 参数是函数，返回值也是函数，是一个装饰器
def copy_properties(src):
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__

    return _copy


def logger(fn):
    @functools.wraps(fn)  # copy_properties的由来,避免函数名和文档出现异常。
    def warg(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)  # 参数解构
        end = datetime.datetime.now()
        print('{} called took {}'.format(fn.__name__, end - start))
        return ret

    return warg


@logger
def sleep(x):
    time.sleep(x)


print(sleep.__name__)  # sleep
