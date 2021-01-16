# -*- coding: utf-8 -*-
# @Time    : 2021/1/16 10:06
# @Author  : wanghc
# @File    : 1.定义.py
# @Software: PyCharm


'''
什么叫反射？   运行时获取类的信息
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self, x, y):
        print(x, y)


p = Point(3, 5)

# 获取p实例的属性  用__dict__
print(p.__dict__)  # {'x': 3, 'y': 5}

# 也可以通过__dict__动态的添加属性
p.__dict__['z'] = 7
print(p.__dict__)  # {'x': 3, 'y': 5, 'z': 7}

# 还可以通过dir(p)查看他的属性和方法，这些都是反射
print(dir(p))
