# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 3.修改.py
@time: 2020/12/24 22:40
"""

'''
当key存在时，对下标赋值就会修改这个key对应的value，这就是字典的修改。
使用update也阔以进行修改。
'''

d = dict(
    name='whc',
    age=18
)

d['age'] = 20
print(d)  # {'name': 'whc', 'age': 20}
