# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: SearchPoi.py
@time: 2021/8/19 21:13
"""
import requests
from pyquery import PyQuery as pq
from requests import RequestException
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
from MySQLTool import MySQL

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s:%(message)s')
BASE_URL = 'https://tianqi.moji.com/weather/china/zhejiang/hangzhou-west-lake-scenic-area-remnant-snow-on-the-broken-bridge'


def request_url(url):
    '''
    :param url:  墨迹天气杭州地区的url
    :return: 对应的html文本文档
    '''
    try:
        logging.info('scraping %s...', url)
        r = requests.get(url=url, timeout=30)
        if r.status_code == 200:
            return r.text
        logging.error('get invalid status code %s while scraping %s...', r.status_code, url)
    except RequestException:
        # 如果出现爬取异常，logging 的 error 方法的 exc_info 参数设置为 True 则可以打印出 Traceback 错误堆栈信息。
        logging.error('error occurred while scraping %s', url, exc_info=True)


def get_weatherinfo(html):
    '''
    :param html: 墨迹天气杭州地区的html文档
    :return: 通过pyquery解析html得到空气质量、温度、天气、湿度、风向
    '''
    doc = pq(html)
    # 空气质量
    quality = doc('.wea_info .wea_alert em').text()
    # 温度
    temperature = doc('.wea_info .wea_weather em').text()
    # 天气
    weather = doc('.wea_info .wea_weather b').text()
    # 湿度
    humidity = doc('.wea_info .wea_about span').text()
    # 风向
    wind_direction = doc('.wea_info .wea_about em').text()
    # 爬取时间
    crawler_time = datetime.datetime.now()

    weather_info = {
        'quality': quality,
        'temperature': temperature,
        'weather': weather,
        'humidity': humidity,
        'wind_direction': wind_direction,
        'crawler_time': crawler_time
    }
    logging.info('get detail weather_info %s', weather_info)
    return weather_info


def save_data(weather_info):
    '''
    :param weather_info: 天气信息字典
    :return: 将天气信息数据插入oracle
    '''
    mysql = MySQL()
    mysql.insert_weatherinfo(weather_info)


def job():
    html = request_url(BASE_URL)
    weather_info = get_weatherinfo(html)
    save_data(weather_info)


# 定义BlockingScheduler
sched = BlockingScheduler()
sched.add_job(job, 'interval', seconds=3600)
sched.start()
