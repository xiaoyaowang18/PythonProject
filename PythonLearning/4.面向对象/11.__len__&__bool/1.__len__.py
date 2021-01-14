# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 20:38
# @Author  : wanghc
# @File    : 1.__len__.py
# @Software: PyCharm


'''
__len__是list中的方法
'''
lst = [1, 2, 3]
print(len(lst))
print(lst.__len__())


class Sized:
    def __len__(self):
        return 10


print(len(Sized()))  # 当对象实现了 __len__方法后，就可以使用内置方法len求对象的长度
