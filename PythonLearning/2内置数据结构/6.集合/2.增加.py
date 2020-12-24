# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 11:29
# @Author  : wanghc
# @File    : 2.增加.py
# @Software: PyCharm


s1 = {1, 2, 3}

s1.add(4)
print(s1)  # {1, 2, 3, 4}
# 增加已存在的元素时,set集合并不会被继续追加新的元素
s1.add(4)
print(s1)  # {1, 2, 3, 4}

# 把自己和别人Union起来
s1.update(range(4, 7))
print(s1)  # {1, 2, 3, 4, 5, 6}
