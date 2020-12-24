# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 17:02
# @Author  : wanghc
# @File    : 2.tuple的陷阱.py
# @Software: PyCharm

# 2 tuple的陷阱

# 当定义一个tuple的时候，tuple的元素就必须被确定下来，比如
t = ('whc','2020加油！')
print(t)

# 如果要定义一个空的tuple，可以写成()
t2 = ()
print(t2)  # ()

# 如果要定义一个只有1个元素的tuple
t3 = (1)
print(t3)  # 1 定义的不是tuple  是1这个数！
'''
因为()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义
因此，python规定，这种情况下按小括号进行计算，计算结果自然是1
所以，只有1个元素的tuple定义时必须加一个逗号，来消除歧义
'''
t4 = (1,)
print(t4) # (1,)   在显示只有1个元素的tuple时，也会加一个逗号，以免误解成数学计算意义上的括号。
