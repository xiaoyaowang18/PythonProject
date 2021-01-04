# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 15:52
# @Author  : wanghc
# @File    : 1.装饰器的副作用.py
# @Software: PyCharm


import datetime
import time

# 定义一个交换name和doc的函数。
def change_properties(one, two):
    one.__name__ = two.__name__
    one.__doc__ = two.__doc__


def logger(fn):
    def warg(*args, **kwargs):
        '''计算sleep时间'''
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)         # 参数解构
        end = datetime.datetime.now()
        print('{} called took {}'.format(fn.__name__, end - start))
        return ret

    #change_properties(warg, fn)
    return warg


@logger
def sleep(x):
    '''sleep函数'''
    time.sleep(x)


print(sleep.__name__)  # warg
print(sleep.__doc__)  # '''计算sleep时间'''

'''
发现name和doc都是warg函数的，不是sleep函数本身的。
可以通过赋值的方式修改过来。保证原函数都能看到他的名字还有doc。
定义一个change_properties函数，赋值修改。
'''


