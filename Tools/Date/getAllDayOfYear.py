# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: getAllDayOfYear.py
@time: 2021/11/3 21:42
"""
import arrow
import datetime


def isLeapYear(years):
    '''
    通过判断闰年，获取年份years下一年的总天数
    :param years: 年份，int
    :return:days_sum，一年的总天数
    '''
    # 断言：年份不为整数时，抛出异常。
    assert isinstance(years, int), "请输入整数年，如 2018"

    if ((years % 4 == 0 and years % 100 != 0) or (years % 400 == 0)):  # 判断是否是闰年
        # print(years, "是闰年")
        days_sum = 366
        return days_sum
    else:
        # print(years, '不是闰年')
        days_sum = 365
        return days_sum


def getAllDayPerYear(year):
    '''
    获取一年的所有日期
    :param years:年份
    :return:全部日期列表
    '''
    start_date = '%s-1-1' % year
    a = 0
    all_date_list = []
    days_sum = isLeapYear(int(year))
    print()
    while a < days_sum:
        b = arrow.get(start_date).shift(days=a).format("YYYY-MM-DD")
        a += 1
        all_date_list.append(b)
    # print(all_date_list)
    return all_date_list


def getALLDayOfYear(years_list):
    '''
    获取各年的所有日期
    :param years_list: 年份列表
    :return: 全部日期列表,date类型
    '''
    all_date_list = []
    for i in years_list:
        date_list = getAllDayPerYear(i)
        for date in date_list:
            all_date_list.append(datetime.date(*map(int, date.split('-'))))
    return all_date_list


if __name__ == '__main__':
    years_list = [2016, 2017, 2018, 2019, 2020, 2021]
    print(getALLDayOfYear(years_list))
