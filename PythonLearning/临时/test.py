# -*- coding: utf-8 -*-
# @Time    : 2020/3/28 14:37
# @Author  : wanghc
# @File    : test.py
# @Software: PyCharm

import time

# 获取本地时间
'''
 localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                              tm_sec,tm_wday,tm_yday,tm_isdst)
'''
localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

# 获取格式化的时间
'''
asctime([tuple]) -> string
Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
'''
localtime2 = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime2)

# 格式化日期
# 格式化成2016-03-20 11:45:39形式
'''
strftime(format[, tuple]) -> string 将时间元组格式化成对应的时间
'''
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 将格式字符串转换为时间戳
a = "2019-12-31 12:00:00"
'''
strptime(string, format) -> struct_time  转换为时间元组
mktime(tuple) -> floating point number 
'''
print(time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S")))



