# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 3.参数解构和可变参数.py
@time: 2020/12/28 22:57
"""


# 定义一个累加器，这个累加器传入了一个可变位置参数，在函数体内部，就是在迭代这个args，因为args是一个元组。

def sum(*args):
    ret = 0
    for i in args:
        ret += i
    return ret


# 用参数解构调用这个函数
# 一个在函数调用时，一个在函数定义时，所以参数解构和可变参数并不冲突
print(sum(*range(10)))
print(sum(*{1, 2, 3}))


def fn(**kwargs):
    print(kwargs)


# 关键字参数解构的时候，key必须是要str，这是需要注意的。

fn(**{'a': 1, 'b': 2})

# 还有一点要注意，当传入的是set的时候，必须保证set顺序和结果没有关系，否则函数体内部的逻辑是否能够按照意愿去迭代就不知道了
