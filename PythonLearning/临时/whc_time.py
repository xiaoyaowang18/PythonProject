# -*- coding: utf-8 -*-
# @Time    : 2020/1/28 21:27
# @Author  : wanghc
# @File    : whc_time.py
# @Software: PyCharm

import time

t = '2020/1/23'
# 先转换为时间数组,然后转换为其他格式
s = time.strptime(t,'%Y/%m/%d')
strtime = time.strftime('%Y%m%d',s)
#print(strtime)

