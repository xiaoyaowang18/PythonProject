# -*- coding: utf-8 -*-
# @Time    : 2021/11/4 15:08
# @Author  : wanghc
# @File    : getDateThree.py
# @Software: PyCharm

import datetime
from datetime import timedelta

'''
根据今天获取去年今天的日期，以及前年今天的日期，且日期标志都是一样
'''


def day_last(date_str):
    year, month, day = date_str.split('-')

    gzr = [1, 2, 3, 4, 5]  # 星期一到星期五
    xxr = [6, 0]  # 星期六、星期天

    today = datetime.date(int(year), int(month), int(day))
    last_week = datetime.date(int(year), int(month), int(day)) - timedelta(weeks=1)
    last_year = datetime.date(int(year) - 1, int(month), int(day))
    twoyear_ago = datetime.date(int(year) - 2, int(month), int(day))

    # 判断当前日期是星期几
    today_week = int(today.strftime('%w'))
    last_year_week = int(last_year.strftime('%w'))
    twoyear_ago_week = int(twoyear_ago.strftime('%w'))

    if today_week in gzr and last_year_week in gzr and twoyear_ago_week in gzr:
        return [last_week.strftime('%Y-%m-%d'), last_year.strftime('%Y-%m-%d'), twoyear_ago.strftime('%Y-%m-%d')]
    elif today_week in gzr and last_year_week in xxr and twoyear_ago_week in gzr:
        if last_year_week == 6:
            last_year_strftime = (last_year - timedelta(days=(last_year_week - today_week))).strftime(
                '%Y-%m-%d')
        elif last_year_week == 0:
            last_year_strftime = (last_year - timedelta(days=int(7 - today_week))).strftime('%Y-%m-%d')
        return [last_week.strftime('%Y-%m-%d'), last_year_strftime, twoyear_ago.strftime('%Y-%m-%d')]
    elif today_week in gzr and last_year_week in gzr and twoyear_ago_week in xxr:
        if twoyear_ago_week == 6:
            twoyear_ago_strftime = (twoyear_ago - timedelta(days=(last_year_week - today_week))).strftime(
                '%Y-%m-%d')
        elif twoyear_ago_week == 0:
            twoyear_ago_strftime = (twoyear_ago - timedelta(days=int(7 - today_week))).strftime('%Y-%m-%d')
        return [last_week.strftime('%Y-%m-%d'), last_year.strftime('%Y-%m-%d'), twoyear_ago_strftime]
    elif today_week in gzr and last_year_week in xxr and twoyear_ago_week in xxr:
        if last_year_week == 6:
            last_year_strftime = (last_year - timedelta(days=(last_year_week - today_week))).strftime(
                '%Y-%m-%d')
        elif last_year_week == 0:
            last_year_strftime = (last_year - timedelta(days=int(7 - today_week))).strftime('%Y-%m-%d')
        if twoyear_ago_week == 6:
            twoyear_ago_strftime = (twoyear_ago - timedelta(days=(last_year_week - today_week))).strftime(
                '%Y-%m-%d')
        elif twoyear_ago_week == 0:
            twoyear_ago_strftime = (twoyear_ago - timedelta(days=int(7 - today_week))).strftime('%Y-%m-%d')
        return [last_week.strftime('%Y-%m-%d'), last_year_strftime, twoyear_ago_strftime]
    elif today_week in xxr and last_year_week in xxr and twoyear_ago_week in xxr:
        return ','.join([last_week.strftime('%Y-%m-%d'), last_year.strftime('%Y-%m-%d'), twoyear_ago.strftime('%Y-%m-%d')])
    elif today_week in xxr and last_year_week in gzr and twoyear_ago_week in xxr:
        if today_week == 6:
            last_year_strftime = (last_year + timedelta(days=(today_week - last_year_week))).strftime(
                '%Y-%m-%d')
        elif today_week == 0:
            last_year_strftime = (last_year + timedelta(days=int(7 - last_year_week))).strftime('%Y-%m-%d')
        return ','.join([last_week.strftime('%Y-%m-%d'), last_year_strftime, twoyear_ago.strftime('%Y-%m-%d')])
    elif today_week in xxr and last_year_week in xxr and twoyear_ago_week in gzr:
        if today_week == 6:
            twoyear_ago_strftime = (twoyear_ago + timedelta(days=(today_week - twoyear_ago_week))).strftime(
                '%Y-%m-%d')
        elif today_week == 0:
            twoyear_ago_strftime = (twoyear_ago + timedelta(days=int(7 - twoyear_ago_week))).strftime('%Y-%m-%d')
        return ','.join([last_week.strftime('%Y-%m-%d'), last_year.strftime('%Y-%m-%d'), twoyear_ago_strftime])
    elif today_week in xxr and last_year_week in gzr and twoyear_ago_week in gzr:
        if today_week == 6:
            twoyear_ago_strftime = (twoyear_ago + timedelta(days=(today_week - twoyear_ago_week))).strftime(
                '%Y-%m-%d')
            last_year_strftime = (last_year + timedelta(days=(today_week - last_year_week))).strftime(
                '%Y-%m-%d')
        elif today_week == 0:
            twoyear_ago_strftime = (twoyear_ago + timedelta(days=int(7 - twoyear_ago_week))).strftime('%Y-%m-%d')
            last_year_strftime = (last_year + timedelta(days=int(7 - last_year_week))).strftime('%Y-%m-%d')
        return ','.join([last_week.strftime('%Y-%m-%d'), last_year_strftime, twoyear_ago_strftime])

print(day_last('2021-11-07'))

