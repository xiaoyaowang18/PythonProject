# -*- coding: utf-8 -*-
# @Time    : 2021/1/16 10:55
# @Author  : wanghc
# @File    : 3.__getattr__&__setattr__&__delattr__.py
# @Software: PyCharm

'''
再来看3个魔术方法：
__getattr__
__setattr__
__hasattr__
'''


class A:
    def __init__(self):
        self.x = 3

    def __getattr__(self, item):
        return 'missing property {}'.format(item)


a = A()
print(a.x)

'''
如果访问a.y肯定会报错，不想让他报错怎么办？
写一个魔术方法__getattr__
'''
# print(a.y)  # missing property y

'''
所以当一个对象定义了__getattr__方法的时候，如果访问不存在的成员，会调用__getattr__方法
'''


# 再来看一种情况
class B:
    NAME = 'B'

    def __init__(self):
        self.x = 5

    def __getattr__(self, item):
        return item


'''
对于b对象来说有多个地方分布着它的属性：
1. __dict__
2. b.__class__.__dict__
3. __getattr__

那么他的属性查找顺序是怎么样的？
b.z的时候，以什么样的顺序来查找？

b.__dict__ > b.__class__.__dict__ > b.__getattr__
'''
b = B()
print(b.x)  # 5  因为在__dict__中，所以直接返回
print(b.NAME)  # 'B'  在class里
print(b.z)  # z  2个都不在，所以去getattr里找了

''''----------------------------------------------------------------------------------------'''


class C:
    def __init__(self):
        self.x = 3

    def __setattr__(self, key, value):
        print('set {} to {}'.format(key, value))
        self.__dict__[key] = value


c = C()  # 初始化实例的时候打印了 'set x to 3'    说明调用了__setattr__方法

c.y = 4  # 给实例添加属性，也会调用__setattr__方法
print(c.__dict__)  # 这里我们的setter方法只是打印了一句话，并没有修改我们的dict，所以是空的。  所以加上 self.__dict__[key] = value

'''
所以当需要对实例的修改，做一些额外的操作的时候，可以使用__setattr__
但是有一个危险的地方就是在__setattr__调setattr()会发生递归溢出 self.key = value 
一般不太建议用 __setattr__
'''

'''--------------------------------------------------------------------------------'''

'''再来看一个delattr'''

class D:
    def __init__(self):
        self.x = 3

    def __delattr__(self, item):
        print('you can not delete property: {}'.format(item))

'''
我们知道可以用del动态的删除一个对象的属性
当一个类实现了__delattr__这个方法时，删除其实例的属性，会调用此方法。可以动态保护我们的属性不被删除
'''



'''
上面这三个方法用的最多的就是getattr，setattr,delattr基本不用
'''