import copy
l1 = [1,'a',4]
# 切片
l2 = l1[:]
# list函数
l3 = list(l1)
# copy函数
l4 = copy.copy(l1)


l2[1] = 4
print(l1)  # [1, 'a', 4]
print(l2)  # [1, 4, 4]