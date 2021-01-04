# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 15:13
# @Author  : wanghc
# @File    : 2.作用.py
# @Software: PyCharm

import datetime
import time


def logger(fn):
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


logger_sleep = logger(sleep)
# print(logger_sleep(3))

'''
封装的时候需要传入一个新的函数.
重新封装一个sleep，再次调用，看看行不行？ 
发现也是可以的
'''
# sleep = logger(sleep)
sleep(2)  # sleep called took 0:00:02.004691   发现也是Ok的

'''
换一种语法糖：装饰器

需要实现定义好一个logger高阶函数，然后在定义其他函数的时候，用@logger,这种语法糖加在函数上面就好了。

@logger的方式和 sleep = logger(sleep)  是等效的

装饰器接受一个函数作为参数，返回一个函数。

所以只要是参数是函数，返回值是一个函数的函数，就可以作为装饰器。
'''
