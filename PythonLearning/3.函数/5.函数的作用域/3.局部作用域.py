# -*- coding: utf-8 -*-
# @Time    : 2020/12/29 10:58
# @Author  : wanghc
# @File    : 3.局部作用域.py
# @Software: PyCharm

def fn():
    xx = 1
    print(xx)


fn()
# print(xx)  # 直接执行Print(xx)没不行的，因为NameError: name 'xx' is not defined

'''
说明变量的作用域为定义此变量的作用域，说明xx只在fn这个函数中可见

变量的作用域为变量定义同级的作用域，在哪个级别定义，就在哪个级别可见
'''


