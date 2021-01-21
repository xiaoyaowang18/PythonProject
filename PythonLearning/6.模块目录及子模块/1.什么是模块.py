# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 19:45
# @Author  : wanghc
# @File    : 1.什么是模块.py
# @Software: PyCharm

'''
模块和包通常是一回事

完全导入：
import module  import os

部分导入：
from module import sub   from os import path

完全导入和部分导入都可以做别名

'''

import os as system

# 使用别名后，原来的名字就不能用了
print(system.getcwd())
