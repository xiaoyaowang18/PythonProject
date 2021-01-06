# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 17:04
# @Author  : wanghc
# @File    : 3.类中定义方法及调用.py
# @Software: PyCharm

class Door:
    def __init__(self, number, status):
        self.number = number
        self.status = status

    def open(self):
        self.status = 'opening'

    def close(self):
        self.status = 'closed'

d = Door(1301,'closed')
print(d.status)

d.open()
print(d.status)

'''
把open方法写在类里的好处:
1.所有对象都能够调用这个方法
2.面向对象的调用，会自动把类传入第一个参数self
3.命名空间不会冲突
'''