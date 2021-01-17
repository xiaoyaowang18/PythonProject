# -*- coding: utf-8 -*-
# @Time    : 2021/1/17 11:15
# @Author  : wanghc
# @File    : 6.finally.py
# @Software: PyCharm


'''

try语句可以带finally子句，无论是否发生异常，finally语句块都会执行。

所以资源清理的工具一般都会放在finally子句当中
'''

'''
try:
    fd = open('./notexist.txt')
finally:
    fd.close()
'''

'''
会抛出2个异常  1.文件不存在  2.fd没有定义
'''


# 解决方法1  在外部定义一个fd变量
# 解决办法2  在finally中再来一个try..except..


#
def p(x):
    print(x)
    return x


def fn():
    try:
        return p(3)
    finally:
        return p(5)


fn()  # 输出 3 5    为什么？

'''
说明了finally子句会在函数返回结果前执行！

1.try中有return的时候，return会先不执行，会先去执行finally子句中的内容
2.然后finally子句执行了return，就没有try子句中的return的事了
'''
