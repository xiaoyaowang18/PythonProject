# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 10:13
# @Author  : wanghc
# @File    : SeleniumCrawler.py
# @Software: PyCharm

'''
适用场景：
有些情况下，Ajax的一些请求接口可能带有一些加密参数，如token,sign等。如果不分析清楚这些参数是怎么生成的话，
我们就难以模拟和构造这些参数。这时候可以选择selenium驱动浏览器渲染的方式，实现所见及所爬，这样无需关心这个
网页背后发生了什么请求、得到什么数据以及怎么渲染页面这些过程，我们看到的页面就是最终浏览器帮我们模拟了 Ajax 请求
和 JavaScript 渲染得到的最终结果，而 Selenium 正好也能拿到这个最终结果，相当于绕过了 Ajax 请求分析和模拟的阶段，
直达目标。

然而 Selenium 当然也有其局限性，它的爬取效率较低，有些爬取需要模拟浏览器的操作，实现相对烦琐。
不过在某些场景下也不失为一种有效的爬取手段。
'''

from selenium import webdriver
import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urllib.parse import urljoin
from os import makedirs
from os.path import exists
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://dynamic2.scrape.center/page/{page}'
TIME_OUT = 10
TOTAL_PAGE = 10
options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
wait = WebDriverWait(browser, TIME_OUT)
RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)


def scrape_page(url, condition, locator):
    '''
    :param url: 传入的url路径
    :param condition: 页面加载的判定条件，它可以是 expected_conditions 的其中某一项判定条件。
    visibility_of_all_elements_located：表示节点可见
    :param locator: 代表定位器，是一个元组，它可以通过配置查询条件和参数来获取一个或多个节点
    By.CSS_SELECTOR, '#index .item' 则代表通过 CSS 选择器查找 #index .item 来获取列表页所有电影信息节点
    :return:
    '''
    logging.info('scraping %s...', url)
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    '''
    :param page: 列表页的页数
    :return:
    '''
    url = INDEX_URL.format(page=page)
    scrape_page(url, condition=EC.visibility_of_all_elements_located, locator=(By.CSS_SELECTOR, '#index .item'))


def parse_index():
    '''
    :return: 列表页中的所有详情页url路径
    '''
    elements = browser.find_elements_by_css_selector('#index .item .name')
    for element in elements:
        href = element.get_attribute('href')
        yield urljoin(INDEX_URL, href)


def scrape_detail(url):
    '''
    :param url: 详情页url
    :return: 详情页内容
    '''
    scrape_page(url, condition=EC.visibility_of_all_elements_located, locator=(By.TAG_NAME, 'h2'))


def parse_detail():
    '''
    :return:
    url:当前页面的URL
    name:电影名称
    categories：类别
    cover：封面
    score:评分
    drama:简介
    '''
    url = browser.current_url
    name = browser.find_element_by_tag_name('h2').text
    categories = [element.text for element in browser.find_elements_by_css_selector('.categories button span')]
    cover = browser.find_element_by_css_selector('.cover').get_attribute('src')
    score = browser.find_element_by_class_name('score').text
    drama = browser.find_element_by_css_selector('.drama p').text
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }


def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='UTF-8'), ensure_ascii=False, indent=2)


def main():
    try:
        for page in range(1, TOTAL_PAGE + 1):
            scrape_index(page)
            detail_urls = parse_index()
            for detail_url in list(detail_urls):
                logging.info('get detail url %s', detail_url)
                scrape_detail(detail_url)
                detail_data = parse_detail()
                save_data(detail_data)
                logging.info('detail data %s', detail_data)
    finally:
        browser.close()


main()
