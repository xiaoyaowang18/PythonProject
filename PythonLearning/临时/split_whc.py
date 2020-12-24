#! /usr/bin/env python
# encoding: utf-8
# @Time ：  

__author__ = 'whc'

def split(s,sep,maxsplit):
    # result用来保存最终结果
    result = []
    # tmp 用来临时保存循环字符串
    tmp = []
    # 计分割次数
    x = 0
    for i in s:
        if i!= sep:
            tmp.append(i)
        else:
            x += 1
            result.append(''.join(tmp))
            tmp.clear() #记得清空字符串
        if x >= maxsplit and x> 0:
            return result
    return result

y = '人人    都是 pythonista'

#print(y.rsplit())
s= ''
print(help(s.casefold()))