# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:16:42 2021
使用Luhn规则校验IMEI码
@author: 18768191466
"""
from odps.udf import annotate
import re

@annotate("string->boolean")
class PyCheckIMEI(object):
    def evaluate(self, card_num):
        if card_num:
            card_num = card_num.strip()
            if bool(re.match(r'^\d+$', card_num)):
                if len(card_num)>=15:
                    vl_Sum1, vl_Sum2 = 0, 0
                    for i in range(14):
                        if ((i % 2)==0):
                            vl_Sum1 += int(card_num[i])
                        else:
                            vl_Temp = int(card_num[i])*2
                            if vl_Temp < 10:
                                vl_Sum2 += vl_Temp
                            else:
                                vl_Sum2 += 1 + vl_Temp - 10
                    vl_Total = vl_Sum1 + vl_Sum2
                    if vl_Total % 10 ==0:
                        if card_num[14] == '0':
                            return True
                    else:
                        if (10 - vl_Total % 10) == int(card_num[14]):
                            return True
                else:
                    return True
        return False
