# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: crawler.py
@time: 2021/10/10 14:06
"""

import requests
import logging
import re
import pymongo
from pyquery import PyQuery as pq
from urllib.parse import urljoin
import multiprocessing

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s:%(message)s')
BASE_URL = 'https://static1.scrape.center'
TOTAL_PAGE = 10
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'movies'
MONGO_COLLECTION_NAME = 'movies'
client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['movies']
collection = db['movies']

'''
传入Url,返回页面的html代码
'''


def scrape_page(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s...', response.status_code, url)
    except requests.RequestException:
        # 如果出现爬取异常，logging 的 error 方法的 exc_info 参数设置为 True 则可以打印出 Traceback 错误堆栈信息。
        logging.error('error occurred while scraping %s', url, exc_info=True)


'''
列表页的爬取方法
'''


def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


'''
解析列表页，得到每部电影的详情页URL
'''


def parse_index(html):
    doc = pq(html)
    links = doc('.el-card .name')
    for link in links.items():
        href = link.attr('href')
        detail_url = urljoin(BASE_URL, href)
        logging.info('get detail url %s', detail_url)
        yield detail_url


def scrape_detail(url):
    return scrape_page(url)


'''
解析详情页，得到我们想要的信息
'''


def parse_detail(html):
    doc = pq(html)
    cover = doc('img .cover').attr('src')  # 封面
    name = doc('a > h2').text()  # 名称
    categories = [item.text() for item in doc('.categories button span').items()]  # 类别
    published_at = doc('.info:contains(上映)').text()  # 上映时间
    published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
        if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None
    drama = doc('.drama p').text()  # 简介
    score = doc('p.score').text()  # 评分
    score = float(score) if score else None
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }


'''
将结果保存到mongodb
$set 操作符表示更新操作；第 3 个参数很关键，这里实际上是 upsert 参数，如果把这个设置为 True，则可以做到存在即更新，不存在即插入的功能，
更新会根据第一个参数设置的 name 字段，所以这样可以防止数据库中出现同名的电影数据。
'''


def save_data(data):
    collection.update_one({

        'name': data.get('name')

    }, {

        '$set': data

    }, upsert=True)


def main(page):
    index_url = scrape_index(page)
    detail_urls = parse_index(index_url)
    # logging.info('detail urls %s', list(detail_urls))
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('get detail data %s', data)
        logging.info('saving data to mongodb')
        save_data(data)
        logging.info('data saved successfully')


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1, TOTAL_PAGE + 1)
    pool.map(main, pages)  # 第 1 个参数就是需要被调用的方法，第 2 个参数就是 pages，即需要遍历的页码。
    pool.close()
    pool.join()
