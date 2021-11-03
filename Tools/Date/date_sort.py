# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: date_sort.py
@time: 2021/11/3 21:11
"""
import datetime
from chinese_calendar import is_workday
from chinese_calendar import is_holiday
from Tools.Date.getAllDayOfYear import getALLDayOfYear
import chinese_calendar as calendar

holidays = {
    "New Year's Day": "元旦",
    "Spring Festival": "春节",
    "Tomb-sweeping Day": "清明节",
    "Labour Day": "劳动节",
    "Dragon Boat Festival": "端午节",
    "National Day": "国庆节",
    "Mid-autumn Festival": "中秋节"
}


def day_sort(date):
    '''
    :param date: date类型的时间
    :return:
    这个date是否是工作日
    是否是休息日
    如果是节假日，是哪个节假日
    '''
    on_workday = is_workday(date)
    on_holiday = is_holiday(date)
    holiday_name = calendar.get_holiday_detail(date)
    date_dict = {}
    date_dict['date'] = date.strftime('%Y-%m-%d')
    date_dict['工作日'] = on_workday
    date_dict['休息日'] = on_holiday
    if holiday_name[1] is not None:
        date_dict['节假日'] = holidays[holiday_name[1]]
    return date_dict


if __name__ == '__main__':
    years_list = [2016, 2017, 2018, 2019, 2020, 2021]
    dates_list = getALLDayOfYear(years_list)
    allday = []
    for date in dates_list:
        daysort = day_sort(date)
        allday.append(daysort)
    print(allday)
