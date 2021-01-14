# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 19:50
# @Author  : wanghc
# @File    : 1.__hash__.py
# @Software: PyCharm


'''
特殊的运算符不能重载：身份运算符不能重载，逻辑运算符不能重载。
'''


# 所有的object都有一个叫hash的方法，所有的类都继承我们的object
class Point:
    # 重写hash方法 。  需要注意： 必须返回int
    def __hash__(self):
        return 1


print(hash(Point()))  # 输出1

# 说明使用内置函数hash对某个对象求hash值，会调用对象的__hash__方法。


'''
set dict的key是需要可hash的，那什么样的对象可hash呢?

可hash对象，就是具有__hash__方法的对象。
'''


class Point2:
    __hash__ = None


# print(set([Point2()]))  将hash置为None,这样才能让类变为不可hash对象。


class Point3:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash('{}:{}'.format(self.x, self.y))


p1 = Point3(1, 2)
p2 = Point3(1, 2)
# 这两个点在平面解析上算是同一个点，这时候可以用set集合来去重，但是由于他们的hash值不同，无法去重，所以这时候可以重写hash方法

print(hash(p1) == hash(p2))  # 重写hash方法后，发现hash值是相等的。
