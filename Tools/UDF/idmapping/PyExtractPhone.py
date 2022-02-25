# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:16:16 2021
抽取手机号码
@author: 18768191466
"""
from odps.udf import annotate
import re

# 手机号匹配的正则表达式
PHONE_REGEX = r'(?:\+?86)?1(?:3[0-9]{3}|5[01235-9][0-9]{2}|8[0-9]{3}|7(?:[0-35-9][0-9]{2}|4(?:0[0-9]|1[0-2]|9[0-9]))|9[0-35-9][0-9]{2}|6[2567][0-9]{2}|4[579][0-9]{2})[0-9]{6}'

@annotate("string->string")
class PyExtractPhone(object):
    """ 抽取手机号码 """

    def evaluate(self, arg0):
        if arg0:
            result = re.findall(PHONE_REGEX, arg0)
            if result:
                return result[0] # ','.join(result)
        return None
        