# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 14:55
# @Author  : wanghc
# @File    : 1.定义.py
# @Software: PyCharm

'''
参数是函数，返回值也是函数
'''


def logger(fn):
    def warg(*args, **kwargs):
        print('call {}'.format(fn.__name__))
        ret = fn(*args, **kwargs)                   # 参数解构
        print('{} called'.format(fn.__name__))
        return ret

    return warg


def add(x, y):
    return x + y


logger_add = logger(add)
print(logger_add)               # <function logger.<locals>.warg at 0x0000023DE07D1AE8>
print(logger_add(3, 5))

'''
这种场景通常用于参数的函数执行前后需要一些额外的操作。
比如我们希望在执行add参数之前打印一些内容出来，因此打印一些内容就被我们称为额外操作。
'''
