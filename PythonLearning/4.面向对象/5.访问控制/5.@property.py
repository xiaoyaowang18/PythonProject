# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 5.@property.py
@time: 2021/1/7 22:31
"""


class Door:
    def __init__(self, number, status):
        self.__number = number
        self.__status = status

    def open(self):
        self.__status = 'opening'

    def close(self):
        self.__status = 'closed'

    def status(self):
        return self.__status

    @property
    def status(self):
        return self.__status

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if isinstance(number, int) and number > 0 and number < 10000:
            self.__number = number

    @number.deleter
    def number(self):
        print('cant delete')


'''
property装饰器会把一个仅有self参数的函数，变成一个属性。属性的值，是方法的返回值。
'''
d = Door(1303, 'closed')
print(d.status)
# d.status()  # 'str' object is not callable

'''
property装饰器会把我们的方法转换成属性。
并且一旦定义后，就可以用property的setter方法把一个方法转换为对此属性赋值。        
特征：
1.方法名一致
2.property必须在前面
3.还有一个setter方法
'''
d.number = 1201
print(d.number)  # 1201

'''
通过property的delete方法删除属性
'''
del d.number