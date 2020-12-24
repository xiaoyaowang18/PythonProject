# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 22:15
# @Author  : wanghc
# @File    : xxmodule.py
# @Software: PyCharm

import random
import string


def add(a, b):
    '''
    累加器，计算a+b的结果
    '''
    return a + b


def is_digit(s):
    '''
    判断是否为数字
    '''
    return isinstance(s, (int, float))


def get_xnum():
    '''
    获取一个随机0-9数字
    '''
    return random.randint(0, 9)


def get_xwords():
    '''
    获取随机一个英文字母
    '''
    return random.choice(string.ascii_letters + string.digits)
