# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 16:17
# @Author  : wanghc
# @File    : 2.柯里化.py
# @Software: PyCharm


import datetime
import time

'''
觉得怪怪的，还需要写一个函数
'''


# 参数是函数，返回值也是函数，是一个装饰器
def copy_properties(src):
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__

    return _copy


def logger(fn):
    def warg(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)  # 参数解构
        end = datetime.datetime.now()
        print('{} called took {}'.format(fn.__name__, end - start))
        return ret

    copy_properties(fn)(warg)
    return warg


@logger
def sleep(x):
    time.sleep(x)


print(sleep.__name__)  # sleep
