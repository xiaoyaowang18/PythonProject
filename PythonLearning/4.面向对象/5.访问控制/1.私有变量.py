# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 1.私有变量.py
@time: 2021/1/7 21:52
"""


class Door:
    def __init__(self, number, status):
        self.number = number
        self.status = status

    def open(self):
        self.status = 'opening'

    def close(self):
        self.status = 'closed'


door = Door(1303, 'closed')

print(door.status)  # closed

door.status = 'opening'

print(door.status)  # 更改door实例的status后，变成opening。这样属性就无法控制

'''
该怎么做呢？  用双下划线控制
'''


class Door2:
    def __init__(self, number, status):
        self.number = number
        self.__status = status

    def open(self):
        self.__status = 'opening'

    def close(self):
        self.__status = 'closed'

    def status(self):
        return self.__status


d = Door2(1301, 'closed')

# print(d.__status)  # 'Door2' object has no attribute '__status'   发现访问不到 __status

print(d.status())  # closed   通过新定义的status函数，获取__status的值


'''
这里给__status赋值为hhh,打印出来也确实是hhh，但是打印实例的__status变量仍然是closed
这说明 d.__status这里只是赋值操作，并没有改变真正的实例属性。
我们需要修改状态的话只能通过open,close方法去改变了。这种就叫做私有变量

双下划线开始，非双下划綫结尾的都是私有的，在类的外部无法访问。
'''
d.__status = 'hhh'
print(d.__status)   #  hhh
print(d.status())   #  closed

d.open()
print(d.status())  #  opening