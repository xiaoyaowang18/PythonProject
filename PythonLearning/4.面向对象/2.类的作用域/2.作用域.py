# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 2.作用域.py
@time: 2021/1/6 20:41
"""


class E:
    NAME = 'E'

    def __init__(self, name):
        self.name = name


e = E('e')
e2 = E('e2')

print(e2.NAME)  # E

'''
所有的实例共享类变量。
'''

# 假如修改e2.NAME
e2.NAME = 'E2'

print(e.NAME)  # E

'''
发现类变量的值还是E

因为python可以动态的给对象增减属性。
所以e2.NAME = 'E2'就是一个赋值，创建了一个新的变量。
当我们对实例的类变量赋值的时候，其实是给这个实例动态的增加了一个属性，覆盖了类变量。
'''

# 印证
E.NAME = 'HHH'
print(e.NAME)  # HHH
print(e2.NAME)  # E2  发现类变量的值被覆盖了

print(e.__class__.NAME)  # HHH
'''
e.__class__.NAME  这是我们的class属性，所有的类变量都存在于 <实例>.__class__.<类变量>
'''

e.NAME = 'XXX'
print(e.__dict__)  # {'name': 'e', 'NAME': 'XXX'}   说明  e.NAME = 'XXX' 等价于  e.__dict__['NAME'] = 'XXX'

print(e.__class__.NAME)  # HHH   为什么还是HHH？   因为访问的还是类变量的值
print(
    e.__class__.__dict__)  # {'__module__': '__main__', 'NAME': 'HHH', '__init__': <function E.__init__ at 0x0000021A4EF0EF70>, '__dict__': <attribute '__dict__' of 'E' objects>, '__weakref__': <attribute '__weakref__' of 'E' objects>, '__doc__': None}

'''
因为他有一个查找顺序：
__class__.__dict__
__dict__

只要我们没有对类的变量进行修改，他永远会去__class__.__dict__去找。
'''
