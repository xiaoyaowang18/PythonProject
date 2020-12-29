# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 14:39
# @Author  : wanghc
# @File    : 8.默认参数作用域.py
# @Software: PyCharm

def fn(x=[]):
    x.append(1)
    print(x)
    return


print(fn())  # [1]
print(fn())  # [1,1]
print(fn())  # [1,1,1]

'''
每次执行fn，发现x这个列表每次都有增加1，没有进行初始化。
在python中一切皆对象，函数也是对象，参数是函数对象的属性，所以函数参数的作用域伴随函数整个生命周期

x是fn中定义的，所以x是fn的一个属性，只要fn存在，x就存在
'''

print(fn.__defaults__)  # ([1, 1, 1],)   # x这个变量保存在__default__属性里面，伴随整个fn的生命周期

'''
什么时候销毁？

对于定义在全局作用里的函数：
1、重新定义
2、del关键字删除
3、程序结束退出

对于局部作用域：
1、重新定义
2、del
3、上级作用域被销毁

'''

'''
使用可变类型作为参数默认值时，需要特别注意
'''


def xy(x=0, y=0):
    x = 3
    y = 3
    print(x, y)


print(xy())  # 3  3
print(xy.__defaults__)  # (0,0)  这里还是0

# 因为x,y是不可变类型

# 上面列表中的append是追加，并没有赋值，所以遇到像列表这种可变类型需要特别注意。

'''
如何解决这种情况？
1.使用不可变类型作为默认值
2.函数体内不改变默认值
'''


# 第一种
def fn1(lst=None):
    if lst is None:
        lst = []
    lst.append(3)
    print(lst)


print(fn1.__defaults__)  # (None,)
print(fn1())  # [3]
print(fn1.__defaults__)  # (None,)


# 第二种
def fn2(lst = []):
    lst = lst[:]
    lst.append(1)
    print(lst)

print(fn2.__defaults__)  # ([],)
print(fn2())  # [1]
print(fn2.__defaults__)  # ([],)


'''
但是2种方式都有缺陷
第一种:如果传入的参数是非Nnone,那么改变了传入参数，这就是副作用

第二种：1.影子拷贝  2.无论如何不传入参数列表


用的最多的就是第一种

通常如果使用一个可变类型作为默认参数时，会使用None来代替
list , byte , bytearray , set
'''