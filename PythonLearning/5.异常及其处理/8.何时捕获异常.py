# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 11:42
# @Author  : wanghc
# @File    : 8.何时捕获异常.py
# @Software: PyCharm

'''
通常有几种情况：
1.需要立即处理的时候
def  parse_int(s):
    try:
        return int(s)
    except:
        return 0

2.在边界处理

什么是边界？

比如一个web应用，边界在哪里？
视图函数
当前线程的最顶层
'''