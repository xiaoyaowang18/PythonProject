# -*- coding: utf-8 -*-

"""
@author: wanghc
@software: PyCharm
@file: 2.增加.py
@time: 2020/12/24 22:29
"""

# 1.可以直接使用key作为下标，对某个不存在的下标赋值，会增加k-v对
d = dict(
    name='whc',
    age=18
)

d['address'] = '杭州'

print(d)  # 输出：{'name': 'whc', 'age': 18, 'address': '杭州'}

# 2.通过update可以同时更新多个键值对，甚至将一个新的字典更新到另一个字典里。
# 如果键存在，就会修改这个键的value
d.update([('weight', 60), ('height', 174)])

print(d)

# 所以update传入参数和dict一样，可以接受一个可迭代对象







