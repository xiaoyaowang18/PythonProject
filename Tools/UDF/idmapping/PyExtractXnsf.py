# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:16:42 2021
针对 安徽_案件基本信息_省厅stkx_smsjzlods_prod.ods_ga_csj_ah_db_ah_2nd_ajjbxx_ds的
saxyxnsf 字段，进行解析，抽取qq、微信号、支付宝账号
@author: 18768191466
"""
from odps.udf import annotate
import re

@annotate("string,string->string")
class PyExtractXnsf(object):
    def evaluate(self, content, e_type):
        """
        Parameters
        ----------
        
        content: 待抽取文本
        e_type: 抽取类型
        """
        if content:
            content = content.decode("utf8")
            res = []
            if e_type == 'qq':
                for part1 in re.split(u'订单号|交易单号|微信|qq群|QQ群|米聊|昵称|千牛账户|支付宝|抖音|微Star|掌嗨|陌陌|通讯号|银行卡|名信|帛发|密码', content):
                    for part2 in re.findall(u'(?<![a-zA-Z0-9_\-])(?:QQ|qq)[^群@]{1}.+', part1):
                        res.extend(re.findall(u'(?<![a-zA-Z0-9_\-])\d{5,}(?![a-zA-Z_\-])',part2))                
            elif e_type == 'wechat':
                for part1 in re.split(u'订单号|交易单号|支付宝账户名|米聊|(?<![a-zA-Z0-9_\-])QQ(?![a-zA-Z_\-]|\.com)|昵称|(?<![a-zA-Z0-9_\-])qq(?![a-zA-Z_\-]|\.com)|千牛账户|抖音|微Star|掌嗨|陌陌|通讯号|银行卡|名信|帛发|密码', content):
                    for part2 in re.findall(u'微信.+', part1):
                        res.extend(re.findall(u'(?<![a-zA-Z0-9_\-])[a-zA-Z][a-zA-Z0-9_\-]{5,19}(?![a-zA-Z0-9_\-])',part2))
            elif e_type == 'alipay':
                for part1 in re.split(u'订单号|交易单号|支付宝账户名|微信|米聊|(?<![a-zA-Z0-9_\-])QQ(?![a-zA-Z_\-]|\.com)|昵称|(?<![a-zA-Z0-9_\-])qq(?![a-zA-Z_\-]|\.com)|千牛账户|抖音|微Star|掌嗨|陌陌|通讯号|银行卡|名信|帛发|密码', content):
                    for part2 in re.findall(u'支付宝.+', part1):
                        res.extend(re.findall(u'(?<![\._\-])[0-9a-zA-Z]+[\-\._0-9a-zA-Z]+@[0-9a-zA-Z]+[\-\.0-9a-zA-Z]*(?:\.[a-z]{2,})+(?![A-Z0-9\._\-])',content))
                        res.extend(re.findall(u'(?<![a-zA-Z0-9_\-])(?:\+?86)?1(?:3[0-9]{3}|5[01235-9][0-9]{2}|8[0-9]{3}|7(?:[0-35-9][0-9]{2}|4(?:0[0-9]|1[0-2]|9[0-9]))|9[0-35-9][0-9]{2}|6[2567][0-9]{2}|4[579][0-9]{2})[0-9]{6}(?![a-zA-Z0-9_\-])',part2))
            elif e_type == 'email':
                res.extend(re.findall(u'(?<![\._\-])[0-9a-zA-Z]+[\-\._0-9a-zA-Z]+@[0-9a-zA-Z]+[\-\.0-9a-zA-Z]*(?:\.[a-z]{2,})+(?![A-Z0-9\._\-])',content))
            if res:
                return ','.join(res)
        return None