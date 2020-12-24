# -*- coding: utf-8 -*-
# @Time    : 2020/1/4 22:43
# @Author  : wanghc
# @File    : 整形和浮点型.py
# @Software: PyCharm

# 1.整形int 不存在溢出  float会溢出，会损失精度   3.3*6 = 19.79999999999999997  变成无限循环小数

from decimal import Context, Decimal
from decimal import getcontext

getcontext().prec = 8

x = Decimal(3.332) * Decimal(6)

print(x)
print(3.3*6)

# 2. None就是一个类型，在判断语句中为False,但None不等于False

# 3. Bool 就是  True or False
