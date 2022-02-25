# -*- coding:utf-8 -*-
from odps.udf import annotate
import re

@annotate("string->string")
class Pysfzh15to18(object):
    """ 15位身份证转18位 """
    def evaluate(self, arg0):
        if isinstance(arg0, str) and len(arg0) == 15:
            arg1 = arg0[:6]+'19'+arg0[6:]
            return arg1 + str(self.get_check_digit(arg1))
        return arg0
    def get_check_digit(self, id_number):
        """ 通过身份证号获取校验码 """
        check_sum = 0
        for i in range(0, 17):
            check_sum += ((1 << (17 - i)) % 11) * int(id_number[i])
        check_digit = (12 - (check_sum % 11)) % 11
        return check_digit if check_digit < 10 else "X"
