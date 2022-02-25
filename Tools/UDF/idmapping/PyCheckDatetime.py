# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:27:40 2021
1. 人-手机号主题表，stkx_sjzldws_dev.idmapping_r_sjh_base，分区dt=‘20210517’中：
   当前的函数无法处理的时间格式有 2535条，总共611045683条记录，予以忽。
   以下是解析不成功的例子：
20161231043029
20170921172610
2018113165144
20170420113916
20171201164649
20161030031419
20171204130635
20171221162621
20180603135431
201853163617
20180409200718
20180413191145
20161023091008
20161023091008
2017/7/1392215

@author: 18768191466
"""
from odps.udf import annotate
import datetime
import re

@annotate("string->string")
class PyCheckDatetime(object):
    """ 转换日期格式到统一的形式 """

    def evaluate(self, arg0):
        if arg0:
            arg0 = arg0.strip()
            if "." in arg0:
                arg0 = arg0[:arg0.index(".")]
            try:
                dt = datetime.datetime.strptime(arg0, '%Y/%m/%d %H:%M:%S')
                return dt.strftime('%Y%m%d%H%M%S')
            except ValueError:
                pass
            try:
                dt = datetime.datetime.strptime(arg0, '%Y/%m/%d%H:%M:%S')
                return dt.strftime('%Y%m%d%H%M%S')
            except ValueError:
                pass        
            try:
                dt = datetime.datetime.strptime(arg0, '%Y-%m-%d %H:%M:%S')
                return dt.strftime('%Y%m%d%H%M%S')
            except ValueError:
                pass
            try:
                dt = datetime.datetime.strptime(arg0, '%Y-%m-%d%H:%M:%S')
                return dt.strftime('%Y%m%d%H%M%S')
            except ValueError:
                pass              
            try:
                dt = datetime.datetime.strptime(arg0, '%Y%m%d%H%M%S')
                return dt.strftime('%Y%m%d%H%M%S')
            except ValueError:
                pass   
            try:
                dt = datetime.datetime.strptime(arg0, '%Y/%m/%d')
                return dt.strftime('%Y%m%d%H%M%S')
            except ValueError:
                pass
            try:
                dt = datetime.datetime.strptime(arg0, '%Y-%m-%d')
                return dt.strftime('%Y%m%d%H%M%S')
            except ValueError:
                pass
            try:
                dt = datetime.datetime.strptime(arg0, '%Y%m%d')
                return dt.strftime('%Y%m%d%H%M%S')
            except ValueError:
                pass
            if "月" in arg0 and "-" in arg0:
                arg0 = re.sub(r' ', '', arg0)
            try:
                dt = datetime.datetime.strptime(arg0, '%d-%m月-%y')
                return dt.strftime('%Y%m%d%H%M%S')
            except ValueError:
                pass
            return None # "20100101000000"
        return None # "20100101000000"
