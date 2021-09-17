# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: SearchXzqh.py.py
@time: 2021/8/20 0:01
"""
import json
import os
import requests
from requests import RequestException
import openpyxl


class SearchXzqh:
    ''' 初始化 省份，下级行政区级数'''

    def __init__(self, keywords, subdistrict, extensions):
        self.keywords = keywords
        self.subdistrict = subdistrict
        self.extensions = extensions

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

    '''省市区县街道'''

    def getXzqh(self):
        url = f'https://restapi.amap.com/v3/config/district?keywords={self.keywords}&subdistrict={self.subdistrict}&key={self.read_key()}'
        result = self.request_api(url)
        list = []
        # 省
        prov_code = result['districts'][0]['adcode']
        prov_name = result['districts'][0]['name']
        prov_jd = result['districts'][0]['center'].split(',')[0]
        prov_wd = result['districts'][0]['center'].split(',')[1]
        list.append([prov_code, prov_name, prov_jd, prov_wd])
        citys = result['districts'][0]['districts']
        for i in range(len(citys)):
            # 市
            city_code = citys[i]['adcode']
            city_name = result['districts'][0]['name'] + citys[i]['name']
            city_jd = citys[i]['center'].split(',')[0]
            city_wd = citys[i]['center'].split(',')[1]
            qxs = citys[i]['districts']
            list.append([city_code, city_name, city_jd, city_wd])
            # print(city_code, city_name, city_jd, city_wd)
            for x in range(len(qxs)):
                # 区县
                qx_code = qxs[x]['adcode']
                qx_name = result['districts'][0]['name'] + citys[i]['name'] + qxs[x]['name']
                qx_jd = qxs[x]['center'].split(',')[0]
                qx_wd = qxs[x]['center'].split(',')[1]
                streets = qxs[x]['districts']
                # print(qx_code, qx_name, qx_jd, qx_wd)
                list.append([qx_code, qx_name, qx_jd, qx_wd])
                for y in range(len(streets)):
                    # 街道
                    street_code = streets[y]['adcode']
                    street_name = result['districts'][0]['name'] + citys[i]['name'] + qxs[x]['name'] + streets[y][
                        'name']
                    street_jd = streets[y]['center'].split(',')[0]
                    street_wd = streets[y]['center'].split(',')[1]
                    list.append([street_code, street_name, street_jd, street_wd])
        return list

    def getCity(self):
        url = f'https://restapi.amap.com/v3/config/district?keywords={self.keywords}&subdistrict={self.subdistrict}&key={self.read_key()}'
        result = self.request_api(url)
        list = []
        citys = result['districts'][0]['districts']
        for i in range(len(citys)):
            # 市
            city_name = citys[i]['name']
            list.append(city_name)
        return list


if __name__ == '__main__':
    list = ['河北省', '山西省', '吉林省', '辽宁省', '黑龙江省', '陕西省', '甘肃省', '青海省', '山东省', '福建省', '浙江省', '河南省', '湖北省', '湖南省', '江西省'
        , '江苏省', '安徽省', '广东省', '海南省', '四川省', '贵州省', '云南省', '台湾省', '北京市', '上海市', '天津市', '重庆市', '内蒙古自治区', '新疆维吾尔自治区'
        , '宁夏回族自治区', '广西壮族自治区', '西藏自治区', '香港特别行政区', '澳门特别行政区']

    wb = openpyxl.Workbook()  # 创建对象
    sheet = wb.active  # 获取默认sheet

    for i in range(len(list)):
        search_city = SearchXzqh(list[i], 2, 'base')
        result = search_city.getXzqh()
        for x in range(len(result)):
            sheet.append(result[x])  # 写入数据，一行
    wb.save("xzqh.xlsx")
