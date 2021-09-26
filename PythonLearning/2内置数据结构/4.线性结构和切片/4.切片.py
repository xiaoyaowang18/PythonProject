# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 10:15
# @Author  : wanghc
# @File    : 4.切片.py
# @Software: PyCharm

l = list(range(10))
print(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9.测试]

# l[start,end] 左开右闭，从start开始，到end结束，不包含end，原地不修改有返回值
l1 = l[3:7]
print(l1)  # [3, 4, 5, 6]

# start为0可以省略
l2 = l[:3]
print(l2)  # [0,1,2]

# 当想获取到最后一个值可以省略end参数
l3 = l[4:]
print(l3)  # [4, 5, 6, 7, 8, 9.测试]

# l[:] 相当于copy方法
l4 = l[:]
print(l4)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9.测试]
l[0] = 'a'
print(l4)  # l修改值,l4不变化 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9.测试]

# start 超出索引范围
l5 = l[-100:3]
print(l5)  # ['a', 1, 2]

# end 超出索引范围
l6 = l[4:1000]
print(l6)  # [4, 5, 6, 7, 8, 9.测试]

# start,end都超出索引范围
l7 = l[-100:100]
print(l7)  # ['a', 1, 2, 3, 4, 5, 6, 7, 8, 9.测试]

'''
结论：
start超出索引范围时，start=0
end超出索引范围，end=-1
'''
# start>=stop 返回空列表
l8 = l[100:-100]
print(l8)  # []

# 负数索引，实际上等于len(list)+index  比如10+(-1)=9.测试
l9 = l[3:-3]
print(l9)  # [3, 4, 5, 6]

l10 = l[-6:-3]  # 等于l[4:7]
print(l10)

l11 = l[3:2]
print(l11)  # []


# 自写函数实现切片功能
def _slice(lst, start=0, end=0):
    # 判断start,end小于0的时候.
    if start < 0:
        start = len(lst) + start
    if end <= 0:
        end = len(lst) + end
    # 判断越界
    if end <= start:
        return []
    if end > len(lst):
        stop = len(lst)

    # 存储切片后的结果
    ret = []

    for i,v in enumerate(lst):
        if i>=start and i <end:
            ret.append(v)

    return ret

# lst[start,end,step] step参数表示一次增加多少
l12 = l[3:8:2]
print(l12)
l13 = l[8:3:-2]
print(l13)
l14 = l[::-1]
print(l14)

# 自己实现一个带step的切片方法

