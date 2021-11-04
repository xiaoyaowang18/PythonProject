# -*- coding: utf-8 -*-
# @Time    : 2021/11/4 15:08
# @Author  : wanghc
# @File    : date_change.py
# @Software: PyCharm

from borax.calendars.lunardate import LunarDate
import datetime

'''
阳历转阴历
'''

today = LunarDate.from_solar_date(2021, 11, 4)

print(today.cn_day)
print(today.cn_year)
print(today.cn_month + '月')
