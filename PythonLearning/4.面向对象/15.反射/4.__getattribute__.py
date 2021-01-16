# -*- coding: utf-8 -*-
# @Time    : 2021/1/16 11:56
# @Author  : wanghc
# @File    : 4.__getattribute__.py
# @Software: PyCharm

'''

__getattribute__最高级别的查找顺序  针对于实例

__getattibute__ > __dict__ > __class__.__dict__ > __getattr__
'''


class A:
    NAME = 'WWW'

    def __init__(self):
        self.x = 3

    def __getattr__(self, item):
        return item

    def __getattribute__(self, name):
        return '哈哈哈'

    def method(self):
        print('method')


a = A()
# 都输出  '哈哈哈'
print(a.x)
print(a.NAME)
print(a.z)
# print(a.method())   连method方法都不能幸免

print(A.NAME)  # 类的属性还是可以的  WWW
