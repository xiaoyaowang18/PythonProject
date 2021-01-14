# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 20:57
# @Author  : wanghc
# @File    : 2.__bool__.py
# @Software: PyCharm

# 先来看一个
if None:
    print('哈哈哈')

'''
None 不是 布尔类型，为什么可以这么写呢？
'''
print(bool(None))  # false
print(bool(0))  # false


class Boolean:
    pass


print(bool(Boolean()))  # True


class A1:
    def __bool__(self):
        return False


class A2:
    def __bool__(self):
        return True


print(bool(A1()))  # False
print(bool(A2()))  # True

print(bool([]))  # False
print(bool([1]))  # True

'''
当对象o实现__bool__方法时，bool(o)的返回值是o.__bool__()
'''


class Sized:
    def __init__(self, size):
        self.size = size

    def __len__(self):
        return self.size


print(bool(Sized(0)))   # False
print(bool(Sized(10)))  # True

'''
总结：
当对象o实现__bool__方法时，bool(o)的返回值是o.__bool__()
当对象没有实现__bool__方法，只实现了__len__方法时，bool(o)的返回值是 len(o) != 0
当对象没有实现__bool__方法，也没有实现__len__方法时，bool(o)的返回值是 True
如果两个方法都实现了，__bool__方法的优先级更高。

因为if while都是默认执行我们的__bool__方法，bool方法必须返回bool类型

以后写类，如果要判断这个类的bool值，或者计算长度，就可以用这2个魔术方法了。
比如：
一个类是Point,需要计算2个点之间的距离，就可以重写__len__方法
'''
