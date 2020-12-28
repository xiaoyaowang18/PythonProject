# -*- coding: utf-8 -*-
# @Time    : 2020/12/28 15:06
# @Author  : wanghc
# @File    : 2.矩阵转置.py
# @Software: PyCharm

'''

将原来的行转成列，原来的列转成行
[[1, 2, 3], [4, 5, 6]]
==》
[[1,4],[2,5],[3,6]]

'''

a = [[1, 2, 3], [4, 5, 6]]
res = []

for i, row in enumerate(a):  # 0 [1,2,3]   1 [4,5,6]
    for j, col in enumerate(row):
        if len(res) - 1 < j:  # 判断这一行能不能用j
            res.append([])
        res[j].append(col)

print(res)
