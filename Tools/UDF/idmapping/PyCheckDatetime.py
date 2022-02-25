# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:27:40 2021
1. ��-�ֻ��������stkx_sjzldws_dev.idmapping_r_sjh_base������dt=��20210517���У�
   ��ǰ�ĺ����޷������ʱ���ʽ�� 2535�����ܹ�611045683����¼�����Ժ���
   �����ǽ������ɹ������ӣ�
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
    """ ת�����ڸ�ʽ��ͳһ����ʽ """

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
            if "��" in arg0 and "-" in arg0:
                arg0 = re.sub(r' ', '', arg0)
            try:
                dt = datetime.datetime.strptime(arg0, '%d-%m��-%y')
                return dt.strftime('%Y%m%d%H%M%S')
            except ValueError:
                pass
            return None # "20100101000000"
        return None # "20100101000000"
