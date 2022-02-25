# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:16:42 2021
针对 执法办案-物品信息表 stkx_smsjzlods_prod.ods_ga_fzzd_zfba_db_gg_wpxx_ds 的
tz字段，进行解析，抽取qq、微信号、支付宝账号、银行卡、imei、imsi、mac、iccid、手机号
@author: 18768191466
"""
from odps.udf import annotate
import re

@annotate("string,string,string->string")
class PyExtractInfo(object):
    def evaluate(self, content, e_type, mode):
        """
        Parameters
        ----------
        
        content: 待抽取文本
        e_type: 抽取类型
        mode: 目前用于银行卡抽取。
        """
        try:
            if content:
                content = content.decode("utf8")
                res = []
                if e_type == 'qq':
                    for part1 in re.split(u'手机|串号|订单号|交易单号|微信|qq群|QQ群|米聊|昵称|千牛账户|支付宝|抖音|微Star|掌嗨|陌陌|通讯号|银行卡|名信|帛发|密码', content):
                        for part2 in re.findall(u'(?<![a-zA-Z0-9_\-])(?:QQ|qq)[^群@]{1}.+', part1):
                            res.extend(re.findall(u'(?<![a-zA-Z0-9_\-])\d{5,}(?![a-zA-Z_\-])',part2))                
                elif e_type == 'wechat':
                    for part1 in re.split(u'手机|串号|订单号|交易单号|支付宝账户名|米聊|(?<![a-zA-Z0-9_\-])QQ(?![a-zA-Z_\-]|\.com)|昵称|(?<![a-zA-Z0-9_\-])qq(?![a-zA-Z_\-]|\.com)|千牛账户|抖音|微Star|掌嗨|陌陌|通讯号|银行卡|名信|帛发|密码', content):
                        for part2 in re.findall(u'微信.+', part1):
                            res.extend(re.findall(u'(?<![a-zA-Z0-9_\-])[a-zA-Z][a-zA-Z0-9_\-]{5,19}(?![a-zA-Z0-9_\-])',part2))
                elif e_type == 'alipay':
                    for part1 in re.split(u'手机|串号|订单号|交易单号|支付宝账户名|微信|米聊|(?<![a-zA-Z0-9_\-])QQ(?![a-zA-Z_\-]|\.com)|昵称|(?<![a-zA-Z0-9_\-])qq(?![a-zA-Z_\-]|\.com)|千牛账户|抖音|微Star|掌嗨|陌陌|通讯号|银行卡|名信|帛发|密码', content):
                        for part2 in re.findall(u'支付宝.+', part1):
                            res.extend(re.findall(u'(?<![\._\-])[0-9a-zA-Z]+[\-\._0-9a-zA-Z]+@[0-9a-zA-Z]+[\-\.0-9a-zA-Z]*(?:\.[a-z]{2,})+(?![A-Z0-9\._\-])',content))
                            res.extend(re.findall(u'(?<![a-zA-Z0-9_\-])(?:\+?86)?1(?:3[0-9]{3}|5[01235-9][0-9]{2}|8[0-9]{3}|7(?:[0-35-9][0-9]{2}|4(?:0[0-9]|1[0-2]|9[0-9]))|9[0-35-9][0-9]{2}|6[2567][0-9]{2}|4[579][0-9]{2})[0-9]{6}(?![a-zA-Z0-9_\-])',part2))
                elif e_type == 'email':
                    res.extend(re.findall(u'(?<![\._\-])[0-9a-zA-Z]+[\-\._0-9a-zA-Z]+@[0-9a-zA-Z]+[\-\.0-9a-zA-Z]*(?:\.[a-z]{2,})+(?![A-Z0-9\._\-])',content))
                elif e_type == 'yhk':
                    if mode == '1':
                        res.extend(re.findall(u'(?<![a-zA-Z0-9_\-\.])[0-9]{5,}(?![a-zA-Z0-9_\-\.])',content))
                    else:
                        for part1 in re.split(u'手机|串号|订单号|交易单号|微信|qq群|QQ群|米聊|昵称|千牛账户|支付宝|抖音|微Star|掌嗨|陌陌|通讯号|银行卡|名信|帛发|密码', content):
                            for part2 in re.findall(u'(?<![a-zA-Z0-9_\-\.])(?:银行)[1-9]?.+', part1):
                                res.extend(re.findall(u'(?<![a-zA-Z0-9_\-\.])[0-9]{5,}(?![a-zA-Z0-9_\-\.])',part2))
                elif e_type == 'imei':
                    for part1 in re.split(u'手机|订单号|交易单号|微信|qq群|QQ群|米聊|昵称|千牛账户|支付宝|抖音|微Star|掌嗨|陌陌|通讯号|银行卡|名信|帛发|密码', content):
                        for part2 in re.findall(u'(?<![a-zA-Z0-9_\-\.])(?:IMEI|imei|串号)[1-9]?.+', part1):
                            res.extend(re.findall(u'(?<![a-zA-Z0-9_\-\.])[0-9]{14,17}(?![a-zA-Z0-9_\-\.])',part2))
                elif e_type == 'imsi':
                    for part1 in re.split(u'手机|串号|订单号|交易单号|微信|qq群|QQ群|米聊|昵称|千牛账户|支付宝|抖音|微Star|掌嗨|陌陌|通讯号|银行卡|名信|帛发|密码', content):
                        for part2 in re.findall(u'(?<![a-zA-Z0-9_\-\.])(?:IMSI|imsi)[1-9]?.+', part1):
                            res.extend(re.findall(u'(?<![a-zA-Z0-9_\-\.])[0-9]{15}(?![a-zA-Z0-9_\-\.])',part2))    
                elif e_type == 'mac':
                    for part1 in re.split(u'手机|串号|订单号|交易单号|微信|qq群|QQ群|米聊|昵称|千牛账户|支付宝|抖音|微Star|掌嗨|陌陌|通讯号|银行卡|名信|帛发|密码', content):
                        for part2 in re.findall(u'(?<![a-zA-Z0-9_\-\.])(?:MAC|mac)[1-9]?.+', part1):
                            res.extend(re.findall(u'(?<![a-zA-Z0-9_\-\.])[0-9ABCDEFabcdef]{2}\:[0-9ABCDEFabcdef]{2}\:[0-9ABCDEFabcdef]{2}\:[0-9ABCDEFabcdef]{2}\:[0-9ABCDEFabcdef]{2}\:[0-9ABCDEFabcdef]{2}(?![a-zA-Z0-9_\-\.])',part2))        
                            res.extend(re.findall(u'(?<![a-zA-Z0-9_\-\.])[0-9ABCDEFabcdef]{2}\-[0-9ABCDEFabcdef]{2}\-[0-9ABCDEFabcdef]{2}\-[0-9ABCDEFabcdef]{2}\-[0-9ABCDEFabcdef]{2}\-[0-9ABCDEFabcdef]{2}(?![a-zA-Z0-9_\-\.])',part2))        
                            res.extend(re.findall(u'(?<![a-zA-Z0-9_\-\.])[0-9ABCDEFabcdef]{12}(?![a-zA-Z0-9_\-\.])',part2))
                    res = [v.upper().replace("-", ":") for v in res]
                    res = [":".join([v[:2],v[2:4],v[4:6],v[6:8],v[8:10],v[10:]]) if len(v) == 12 else v for v in res]               
                elif e_type == 'iccid':
                    for part1 in re.split(u'手机|串号|订单号|交易单号|微信|qq群|QQ群|米聊|昵称|千牛账户|支付宝|抖音|微Star|掌嗨|陌陌|通讯号|银行卡|名信|帛发|密码', content):
                        for part2 in re.findall(u'(?<![a-zA-Z0-9_\-\.])(?:ICCID|iccid)[1-9]?.+', part1):
                            res.extend(re.findall(u'(?<![a-zA-Z0-9_\-\.])[0-9a-z]{19,20}(?![a-zA-Z0-9_\-\.])',part2))                    
                elif e_type == 'sjh':                        
                    for part1 in re.split(u'串号|订单号|交易单号|微信|qq群|QQ群|米聊|昵称|千牛账户|支付宝|抖音|微Star|掌嗨|陌陌|通讯号|银行卡|名信|帛发|密码', content):
                        for part2 in re.findall(u'手机.+', part1):
                            res.extend(re.findall(u'(?<![a-zA-Z0-9_\-\.])(?:\+?86)?1(?:3[0-9]{3}|5[01235-9][0-9]{2}|8[0-9]{3}|7(?:[0-35-9][0-9]{2}|4(?:0[0-9]|1[0-2]|9[0-9]))|9[0-35-9][0-9]{2}|6[2567][0-9]{2}|4[579][0-9]{2})[0-9]{6}(?![a-zA-Z0-9_\-\.])',part2))             
                elif e_type == 'sjh/imei':
                    sjh = []
                    for part1 in re.split(u'串号|订单号|交易单号|微信|qq群|QQ群|米聊|昵称|千牛账户|支付宝|抖音|微Star|掌嗨|陌陌|通讯号|银行卡|名信|帛发|密码', content):
                        for part2 in re.findall(u'手机.+', part1):
                            sjh.extend(re.findall(u'(?<![a-zA-Z0-9_\-\.])(?:\+?86)?1(?:3[0-9]{3}|5[01235-9][0-9]{2}|8[0-9]{3}|7(?:[0-35-9][0-9]{2}|4(?:0[0-9]|1[0-2]|9[0-9]))|9[0-35-9][0-9]{2}|6[2567][0-9]{2}|4[579][0-9]{2})[0-9]{6}(?![a-zA-Z0-9_\-\.])',part2))   
                    imei = []
                    for part1 in re.split(u'手机|订单号|交易单号|微信|qq群|QQ群|米聊|昵称|千牛账户|支付宝|抖音|微Star|掌嗨|陌陌|通讯号|银行卡|名信|帛发|密码', content):
                        for part2 in re.findall(u'(?<![a-zA-Z0-9_\-\.])(?:IMEI|imei|串号)[1-9]?.+', part1):
                            imei.extend(re.findall(u'(?<![a-zA-Z0-9_\-\.])[0-9]{14,17}(?![a-zA-Z0-9_\-\.])',part2))
                    sjh=sjh[::-1]
                    imei=imei[::-1]
                    while imei and sjh:
                        one_sjh = sjh.pop()
                        res.append('%s/%s' % (one_sjh, imei.pop()))
                        if len(imei) > len(sjh):
                            res.append('%s/%s' % (one_sjh, imei.pop()))    
                if res:
                    return ','.join(res)
            return None
        except :
            raise Exception(u"报错, content:{}".format(content))