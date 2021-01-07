# -*- coding: utf-8 -*-
# @Time    : 2021/1/7 14:23
# @Author  : wanghc
# @File    : 1.类装饰器.py
# @Software: PyCharm

'''
假如我们要解决一个类的问题，就可以给类加上装饰器

所以类装饰器通常用于给类增加属性
'''


def set_name(name):
    def wrap(cls):
        cls.NAME = name
        return cls

    return wrap


@set_name('G')
class F:
    pass


f = F()

print(f.NAME)  # G
print(F.NAME)  # G
