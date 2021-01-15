# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 22:03
# @Author  : wanghc
# @File    : 5.__wrapped__.py
# @Software: PyCharm

'''
之前写过装饰器，来对函数进行计时，看他执行了多久

现在来看下上下文管理如何来实现计时
'''
import datetime


class Timeit:
    def __enter__(self):
        self.start = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        cost = datetime.datetime.now() - self.start
        print(cost)


# with  Timeit():
#   z = 3 - 2

'''
这样就通过了上下文管理完成计时，而不是对函数计时了。

如果既想让他像上下文这样计时，又能像装饰器那样怎么办呢？
'''

from functools import wraps


class Timeit2:
    def __init__(self, fn=None):
        # wraps原型是接受柯里化的参数，第一个是包装的函数  第二个是被包装的函数
        # 理解为动态的给self对象添加了一个__wrapped__属性，里面存放包装函数的引用。
        wraps(fn)(self)

    '''
    整合call方法，写成一个通用的装饰器。
    可以对代码块做装饰，也可以对函数进行装饰了
    '''

    def __call__(self, *args, **kwargs):
        start = datetime.datetime.now()
        ret = self.__wrapped__(*args, **kwargs)
        cost = datetime.datetime.now() - start
        print(cost)
        return ret

    def __enter__(self):
        self.start = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        cost = datetime.datetime.now() - self.start
        print(cost)


# with Timeit2():
#   z = 3 + 12312


@Timeit2
def add(x, y):
    return x + y


add(1, 3)

a = Timeit()
wraps(lambda x: x)(a)
print(dir(a))  # 发现新增了wrapped参数 。这样就理解了为什么在call函数中会使用self.__wrapped__



'''
使用场景：
1.凡是在代码块前后插入代码的场景，统统适用
2.资源管理（打开网络连接，数据库连接，都叫做资源类）
3.权限验证（需要在进入代码块之前执行）
'''