# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 14:12:28 2021
从“车辆类型” 向 “机动车号牌种类代码” 进行转化
@author: 18768191466
"""
from odps.udf import annotate
import re

chinese = {
    u'一': u'1',
    u'二': u'2',
    u'三': u'3',
    u'四': u'4',
    u'五': u'5',
    u'六': u'6',
    u'七': u'7',
    u'八': u'8',
    u'九': u'9',
    u'幺': u'1',
    u'拐': u'7',
    u'洞': u'0',
    u'两': u'2',
    u'勾': u'9'
}
# 97式军车牌格式
MILITARY_VEHICLES = u'[甲乙丙己庚壬壬寅辰午未申][A-Z]\d{5}'
MILITARY_VEHICLES_TWO = u'[北沈兰济南广成海空军][A-Z]\d{5}'
# 13式武警车牌
ARMED_POLICE_VEHICLE = u'WJ[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼]\d{4}[XBTSGJD]'
# 新军车牌照
NEW_MILITARY_VEHICLES = u'[ABCGNJLSHK][A-Z]\d{5}'
# 民用车牌
ORDINARY_CAR_RE = u'[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领][A-Z][A-HJ-NP-Z0-9]{4}[A-HJ-NP-Z0-9挂学警港澳]'
# 新能源车牌
NEW_ENERGY_VEHICLE_RE = u'[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领][A-Z](([0-9]{5}[DF])|([DF][A-HJ-NP-Z0-9][0-9]{4}))'
# 农用车牌
CIVIL_CAR_ONE = u'[鄂甘赣渝津苏京豫黑冀琼云吉沪鲁闽贵蒙晋湘浙皖粤桂青新藏川宁陕辽][0-5][0-9]\d{5}'
CIVIL_CAR_TWO = u'(湖北|云南|北京|甘肃|黑龙江|吉林|重庆|湖南|广东|辽宁|河北|宁夏|山东|四川|西藏|新疆|江西|陕西|江苏|上海|天津|内蒙古|海南|山西|福建|广西|青海|贵州|河南|浙江|安徽)[A-Z]\d{5}'
CIVIL_CAR = CIVIL_CAR_ONE + '|' + CIVIL_CAR_TWO
# 摩托车牌
MOBILE_RE = u'[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼学使领警][A-Z][A-HJ-NP-Z0-9]{3}[A-HJ-NP-Z0-9学警港澳领]'

@annotate("string,string->string")
class PyCllx2Hpzl(object):
    def evaluate(self, hphm, cllx):
        """
        Parameters
        ----------
        
        hphm: 号牌号码
        cllx: 车辆类型
        
        """
        if hphm and cllx:
            hphm = ''.join([chinese.get(v, v) for v in hphm.decode("utf8")]).upper()
            hphm = re.sub(r' ', '', hphm)
            cllx = int(cllx)
            # 摩托车
            if bool(re.match(MOBILE_RE, hphm)):
                if hphm[0] == '使':
                    return '09'	#  使馆摩托车
                elif  hphm[-1] == '领':
                    return '10'	#  领馆摩托车
                elif hphm[-1] == '学':
                    return '17'	#  教练摩托车
                elif hphm[-1] == '警':
                    return '24'  #	警用摩托
                else: #其它类型摩托车类型的车牌 无法判断
                    return '07'	#  普通摩托车
            # 机动车
            else:
                if hphm[0] == '使':
                    return '03'	#  使馆汽车
                elif  hphm[-1] == '领':
                    return '04'   #	领馆汽车
                if bool(re.match(MILITARY_VEHICLES, hphm)) or\
                bool(re.match(NEW_MILITARY_VEHICLES, hphm)) or\
                bool(re.match(MILITARY_VEHICLES_TWO, hphm)):
                    return '32'	    #  军队号牌
                if bool(re.match(ARMED_POLICE_VEHICLE, hphm)):
                    return '31'      #	武警号牌
                if bool(re.match(ORDINARY_CAR_RE, hphm)):
                    if  hphm[-1] == '挂':
                        return '15	'#  挂车
                    elif hphm[-1] == '学':
                        return '16'	#  教练汽车
                    elif hphm[-1] == '警':
                        return '23'	#  警用汽车
                    elif hphm[-1] == '港':
                        return '26'	#  香港入出境车
                    elif hphm[-1] == '澳':
                        return '27'	#  澳门入出境车
                if bool(re.match(CIVIL_CAR, hphm)):
                    return '25'      # 	原农机号牌
                # 客车、货车、大客车、大货车、中型车、大型车、中巴车
                if cllx in (3, 2, 16, 17, 2, 15):
                    if bool(re.match(NEW_ENERGY_VEHICLE_RE, hphm)):
                        return '51'	#  大型新能源汽车
                    return '01'   #	大型汽车
                # 轿车、suv、小货车、面包车
                if cllx in (1, 11, 12, 14, 13):
                    if bool(re.match(NEW_ENERGY_VEHICLE_RE, hphm)):
                        return '52'	#  小型新能源汽车
                    return '02'   #	大型汽车                    
        return '99'
            