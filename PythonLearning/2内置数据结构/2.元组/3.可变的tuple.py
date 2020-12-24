# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 17:02
# @Author  : wanghc
# @File    : 3.可变的tuple.py
# @Software: PyCharm

# 3 可变的tuple
t5 = ('whc','wvely',['2020','加油！'])
t5[2][1] = '加油啊！'
print(t5)  # ('whc', 'wvely', ['2020', '加油啊！'])
'''
表面上看tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素
tuple一开始指向的list并没有改成别的list
所以tuple所谓的不变是说：tuple的每个元素指向永远不变。
指向一个list,就不能改成指向其他对象，但是这个list本身是可变的！
'''

# 如果要创建一个内容也不变的tuple，那就必须要保证tuple的每个元素本身也不能变