# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 10:16
# @Author  : wanghc
# @File    : 3.如何捕获异常.py
# @Software: PyCharm

'''
所谓捕获异常，就是对异常做处理

一个健壮的程序是妥善处理了各种异常的，至少有3分之一的时间是考虑如何处理错误
'''

'''
try:
    可能抛出异常的代码
except:
    对异常的处理
'''

# try块会执行到抛出异常的行
# except可以做模式匹配，匹配特定的异常类型
try:
    print('start')
    raise Exception()
    print('end')
except:
    print('except')
