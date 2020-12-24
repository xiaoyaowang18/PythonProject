# -*- coding: utf-8 -*-
# @Time    : 2020/3/27 17:26
# @Author  : wanghc
# @File    : bhyy0003.py
# @Software: PyCharm

import time, datetime
from dateutil.relativedelta import relativedelta

'''
需求：
通过一延开始日期，根据规则计算出一延截止日期

例：
加一个月，减一天  
2019-12-06   2020-01-05
无对应日期的，以该月的最后一日为截止日。
2019-01-31   2020-02-29
'''


def Not_OneMonth(yyksrq):
    # 先转换为时间元组，再将时间元组格式化  2020-03-28  或者直接截取日期前几位也可
    trans_ksrq = time.strftime('%Y-%m-%d', time.strptime(yyksrq, '%Y-%m-%d %H:%M:%S'))

    list_time = trans_ksrq.split('-')

    # 将字符串时间，转换为date类型
    date_ksrq = datetime.date(*map(int, list_time))

    # 1.正常情况下加一个月，减一天就是截止日期
    # 2.不正常情况比如正常年份 1-29 1-30 1-31   加一个月就行
    # 3.不正常情况比如闰年 1-30 1-31   加一个月就行
    year = int(list_time[0])

    if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        if trans_ksrq[5:] in ['01-30', '01-31']:
            date_jsrq = date_ksrq + relativedelta(months=1)
        else:
            date_jsrq = date_ksrq + relativedelta(months=1) - datetime.timedelta(days=1)
    else:
        if trans_ksrq[5:] in ['01-29', '01-30', '01-31']:
            date_jsrq = date_ksrq + relativedelta(months=1)
        else:
            date_jsrq = date_ksrq + relativedelta(months=1) - datetime.timedelta(days=1)

    return date_ksrq, date_jsrq


