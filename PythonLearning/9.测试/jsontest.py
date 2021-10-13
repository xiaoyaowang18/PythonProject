# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 15:07
# @Author  : wanghc
# @File    : jsontest.py
# @Software: PyCharm

import json

str = {'article': '中华人民共和国共和国万岁', 'tag': '中国共产党万岁'}
# 将python对象格式化成json字符串
encoded_json = json.dumps(str, ensure_ascii=False)
print(encoded_json, type(encoded_json))

# 将json字符串解码成python对象
decode_json = json.loads(encoded_json)
print(decode_json, type(decode_json))

# json.dump主要用来将python对象写入json文件
f = open('demo.json', 'w', encoding='utf-8')
json.dump(decode_json, f, ensure_ascii=False)
f.close()

# json.load加载json格式文件，返回python对象
f = open('demo.json', 'r', encoding='utf-8')
data = json.load(f)
print(data, type(data))
f.close()
