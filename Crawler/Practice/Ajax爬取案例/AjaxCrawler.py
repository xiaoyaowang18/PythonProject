# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 10:53
# @Author  : wanghc
# @File    : AjaxCrawler.py
# @Software: PyCharm

import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://dynamic1.scrape.center/api/movie/?limit={limit}&offset={offset}'
DETAIL_URL = 'https://dynamic1.scrape.center/api/movie/{id}'
INDEX_LIMIT = 10
TOTAL_PAGE = 10

'''
1、定义一个通用的爬取方法
'''


def crawler_api(url):
    logging.info('scraping %s...', url)
    try:
        logging.captureWarnings(True)
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        logging.error('get invalid status_code while scraping %s...', url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s...', url)


'''
2、爬取列表页
'''


def crawler_index(page):
    url = INDEX_URL.format(limit=INDEX_LIMIT, offset=INDEX_LIMIT * (page - 1))
    return crawler_api(url)


'''
3、爬取详情页
'''


def crawler_detail(id):
    url = DETAIL_URL.format(id=id)
    return crawler_api(url)


'''
4、总的调用方法
'''


def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_data = crawler_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = crawler_detail(id)
            logging.info('detail data %s', detail_data)


if __name__ == '__main__':
    main()
