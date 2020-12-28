# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 4.函数的嵌套.py
@time: 2020/12/28 23:46
"""

'''
函数内可以嵌套函数
'''


def outter():
    def inner():
        print('inner')

    print('outter')
    inner()
