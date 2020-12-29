# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 11:42
# @Author  : wanghc
# @File    : 5.全局变量global.py
# @Software: PyCharm

'''
全局变量可以让我们对所有作用域可见
'''

xx = 1


def fn():
    global xx
    xx += 1
    print(xx)


fn()  # xx变成了2

'''
所以global关键字可以提升变量作用域为全局变量
'''


def fn2():
    global zz
    zz = 3
    print(zz)


def fn3():
    print(zz)


fn2()
fn3()  # fn3函数拿到了全局变量zz   输出3


def fn4():
    zz += 1
    print(zz)

# fn4()  # 报错  UnboundLocalError: local variable 'zz' referenced before assignment


'''
global提升只对本作用域有用，如果需要他在其他局部作用域有用，需要再标记
'''

def fn5():
    global zz
    zz += 1
    print(zz)

fn5()



'''
除非清楚的知道，global会带来什么，并且明确的知道非global不行，否则不要使用global
'''