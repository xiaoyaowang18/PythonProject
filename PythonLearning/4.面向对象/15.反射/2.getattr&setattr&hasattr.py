# -*- coding: utf-8 -*-
# @Time    : 2021/1/16 10:21
# @Author  : wanghc
# @File    : 2.getattr&setattr&hasattr.py
# @Software: PyCharm


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self, x, y):
        print(x, y)


# 1.getattr
# 如果想通过print这个方法名称，获取print方法？  这个时候就该getattr登场了
'''
getattr接受3个参数：
1.参数成员对象
2.对象方法
3.成员名称，可以忽略
'''
p = Point(1, 2)
print(getattr(p, 'print', p))  # <bound method Point.print of <__main__.Point object at 0x000001E44BAC7FD0>>

# 看一下能不能获取属性？
print(getattr(p, 'x'))  # 1  也是能够获取到的

'''
可以发现getattr无论是成员对象的属性还是方法，都可以获取到。
'''

# 2.setattr
setattr(p, 'z', '3')  # 等价于p.z = 3
print(p.z)

# 3.hasattr  看成员没有这个属性
print(hasattr(p,'c'))  # false

'''
setattr只能创建属性不能创建方法，为什么呢？
setattr的对象是一个实例，实例是无法动态添加方法的。
来看一下有没有别的方法可以做到？
'''
def mm(self):
    print(self.x)

import types
# 给实例动态添加方法，需要先把函数转化为方法，转换的方法是types.MethodType()  但基本不太用
setattr(p,'mm',types.MethodType(mm,p))
p.mm()

'''
通常getattr和setattr都是对已存在的属性操作的，不太会对实例动态增减属性
'''

