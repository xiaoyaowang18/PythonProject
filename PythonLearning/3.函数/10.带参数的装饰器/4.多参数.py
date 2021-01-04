# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 4.多参数.py
@time: 2021/1/4 21:53
"""
import datetime
import functools
import time

'''
将超时的逻辑抽取出来，日志打印更加灵活了。

假如数据库有一个慢查询定义2秒，生产环境去看日志就不切实际了，这个时候可以让它往监控库发，超过2秒就发。
发的这个动作写在参数P中。

所以这个装饰器是一个监视慢查询的装饰器。
'''
def _log(s,p=lambda name,t : print('{} call took {}'.format(name,t))):
    def logger(fn):
        @functools.wraps(fn)
        def wrag(*args, **kwargs):
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            end = datetime.datetime.now()
            if (end - start).total_seconds() > s:
                p(fn.__name__, end - start)
            return ret

        return wrag

    return logger

@_log(2)
def sleep(x):
    time.sleep(x)

sleep(3)