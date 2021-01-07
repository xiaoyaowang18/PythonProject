# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 2.访问控制.py
@time: 2021/1/7 22:11
"""


class Door:
    def __init__(self, number, status):
        self.number = number
        self.__status = status

    def open(self):
        self.__status = 'opening'

    def close(self):
        self.__status = 'closed'

    def status(self):
        return self.__status


d = Door(1301, 'closed')
'''
我们知道通过 实例d 直接去访问属性  __status  是访问不到的。
'''
# print(d.__status)  # 'Door' object has no attribute '__status'

'''
但是python非常巧妙，有其他方式可以访问到。  _类名+带双下划线 就能访问到我们的类私有变量了
从严格意义上来说，python没有真正的私有成员。
除非真的有必要，否则不要这么做。因为这样就破坏了类的封装。
'''
print(d._Door__status)  # closed
d._Door__status = 'opening'
print(d.status())  # opening  发现是可以改变的
