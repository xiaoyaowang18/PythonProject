# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: SearchPoi.py
@time: 2021/8/19 21:13
"""
import os
import openpyxl
import requests
from requests import RequestException
import json
import math
from Crawler.GdAPI.SearchXzqh import SearchXzqh


class SearchPoi:
    ''' 初始化 关键字，poi类型，城市，分页记录条数'''

    def __init__(self, keywords, types, cityname, page_size):
        self.keywords = keywords
        self.types = types
        self.cityname = cityname
        self.page_size = page_size

    '''获取Key'''

    def read_key(self):
        """将key持久化"""
        key_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'user-key')
        with open(key_path, 'r', encoding='utf-8') as f:
            key = f.read()
        return key

    '''请求url 返回text'''

    def request_url(self, url):
        try:
            r = requests.get(url=url, timeout=30)
            if r.status_code == 200:
                return r.text
            return None
        except RequestException:
            print("请求url错误异常")
            return None

    ''' 解析json，返回dict'''

    def parse_json(self, content_json):
        reuslt_json = json.loads(content_json)
        return reuslt_json

    def request_api(self, url):
        reuslt = self.request_url(url)
        result_josn = self.parse_json(reuslt)
        return result_josn

    def getPoiResult(self):
        url = f'https://restapi.amap.com/v3/place/text?keywords={self.keywords}&types={self.types}&city={self.cityname}&offset={self.page_size}&page=1&key={self.read_key()}&extensions=base&city_limit=true'
        index_result = self.request_api(url)
        '''计算要访问多少页   count返回总量数 / page_size每页记录数'''
        pages = math.ceil(int(index_result['count']) / self.page_size)
        print(int(index_result['count']))
        print(pages)
        list = []
        for page in range(1, pages+1):
            url = f'https://restapi.amap.com/v3/place/text?keywords={self.keywords}&types={self.types}&city={self.cityname}&offset={self.page_size}&page={page}&key={self.read_key()}&extensions=base&city_limit=true'
            result = self.request_api(url)
            poiss = result['pois']
            for i in range(len(poiss)):
                pois_name = poiss[i]['name']
                pois_jd = poiss[i]['location'].split(',')[0]
                pois_wd = poiss[i]['location'].split(',')[1]
                xzqhmc = poiss[i]['pname'] + poiss[i]['cityname'] + poiss[i]['adname'] + poiss[i]['name']
                list.append((pois_name, xzqhmc, pois_jd, pois_wd))
        return list


if __name__ == '__main__':
    '''获取各地市学校数据'''
    wb = openpyxl.Workbook()  # 创建对象
    sheet = wb.active  # 获取默认sheet
    search_city = SearchXzqh('浙江', 1, 'base')
    citys = search_city.getCity()
    for i in range(len(citys)):
        search_schools = SearchPoi('学校', 141200, citys[i], 20)
        schools = search_schools.getPoiResult()
        for y in range(len(schools)):
            sheet.append(schools[y])  # 写入数据，一行
    wb.save("schools.xlsx")