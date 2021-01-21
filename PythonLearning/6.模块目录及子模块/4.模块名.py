# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 20:09
# @Author  : wanghc
# @File    : 4.模块名.py
# @Software: PyCharm

'''
1.在python中，python文件即模块，模块名即文件名
2.又因为文件名是模块名，所以要求文件名必须符合python标识符规范，否则无法导入
'''

'''
例如：
新建一个os.py  新建的os文件就代替了原系统的os模块，因为python是对我们自己创建的模块查找的


'''

import sys

for line in sys.path:
    print(line)

'''
sys.path指定了模块的查找路径，当我们import的时候，会根据我们的sys.path找文件，找到就返回。需要注意的是，不包括子目录
'''

'''
自定义模块是一个python文件
自定义模块的文件必须符合python标识符规范
应该避免命名冲突
'''