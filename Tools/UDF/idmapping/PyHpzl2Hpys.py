# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 17:53:08 2021
∫≈≈∆÷÷¿‡ ◊™ ∫≈≈∆—’…´
@author: 18768191466
"""
from odps.udf import annotate
import re

chinese = {
    u'“ª': u'1',
    u'∂˛': u'2',
    u'»˝': u'3',
    u'Àƒ': u'4',
    u'ŒÂ': u'5',
    u'¡˘': u'6',
    u'∆ﬂ': u'7',
    u'∞À': u'8',
    u'æ≈': u'9',
    u'Á€': u'1',
    u'π’': u'7',
    u'∂¥': u'0',
    u'¡Ω': u'2',
    u'π¥': u'9'
}
# 97 Ωæ¸≥µ≈∆∏Ò Ω
MILITARY_VEHICLES = u'[º◊““±˚º∫∏˝»…»…“˙≥ΩŒÁŒ¥…Í][A-Z]\d{5}'
MILITARY_VEHICLES_TWO = u'[±±…Ú¿ºº√ƒœπ„≥…∫£ø’æ¸][A-Z]\d{5}'
# 13 ΩŒ‰æØ≥µ≈∆
ARMED_POLICE_VEHICLE = u'WJ[æ©ΩÚª¶”ÂºΩ‘•‘∆¡…∫⁄œÊÕÓ¬≥–¬À’’„∏”∂ıπ∏ Ω˙√……¬º™√ˆπÛ‘¡«‡≤ÿ¥®ƒ˛«Ì]\d{4}[XBTSGJD]'
# –¬æ¸≥µ≈∆’’
NEW_MILITARY_VEHICLES = u'[ABCGNJLSHK][A-Z]\d{5}'
# √Ò”√≥µ≈∆
ORDINARY_CAR_RE = u'[æ©ΩÚª¶”ÂºΩ‘•‘∆¡…∫⁄œÊÕÓ¬≥–¬À’’„∏”∂ıπ∏ Ω˙√……¬º™√ˆπÛ‘¡«‡≤ÿ¥®ƒ˛«Ì π¡Ï][A-Z][A-HJ-NP-Z0-9]{4}[A-HJ-NP-Z0-9π“—ßæØ∏€∞ƒ]'
# –¬ƒ‹‘¥≥µ≈∆
NEW_ENERGY_VEHICLE_RE = u'[æ©ΩÚª¶”ÂºΩ‘•‘∆¡…∫⁄œÊÕÓ¬≥–¬À’’„∏”∂ıπ∏ Ω˙√……¬º™√ˆπÛ‘¡«‡≤ÿ¥®ƒ˛«Ì π¡Ï][A-Z](([0-9]{5}[DF])|([DF][A-HJ-NP-Z0-9][0-9]{4}))'
# ≈©”√≥µ≈∆
CIVIL_CAR_ONE = u'[∂ı∏ ∏””ÂΩÚÀ’æ©‘•∫⁄ºΩ«Ì‘∆º™ª¶¬≥√ˆπÛ√…Ω˙œÊ’„ÕÓ‘¡π«‡–¬≤ÿ¥®ƒ˛…¬¡…][0-5][0-9]\d{5}'
CIVIL_CAR_TWO = u'(∫˛±±|‘∆ƒœ|±±æ©|∏ À‡|∫⁄¡˙Ω≠|º™¡÷|÷ÿ«Ï|∫˛ƒœ|π„∂´|¡…ƒ˛|∫”±±|ƒ˛œƒ|…Ω∂´|Àƒ¥®|Œ˜≤ÿ|–¬ΩÆ|Ω≠Œ˜|…¬Œ˜|Ω≠À’|…œ∫£|ÃÏΩÚ|ƒ⁄√…π≈|∫£ƒœ|…ΩŒ˜|∏£Ω®|π„Œ˜|«‡∫£|πÛ÷›|∫”ƒœ|’„Ω≠|∞≤ª’)[A-Z]\d{5}'
CIVIL_CAR = CIVIL_CAR_ONE + '|' + CIVIL_CAR_TWO
# ƒ¶Õ–≥µ≈∆
MOBILE_RE = u'[æ©ΩÚª¶”ÂºΩ‘•‘∆¡…∫⁄œÊÕÓ¬≥–¬À’’„∏”∂ıπ∏ Ω˙√……¬º™√ˆπÛ‘¡«‡≤ÿ¥®ƒ˛«Ì—ß π¡ÏæØ][A-Z][A-HJ-NP-Z0-9]{3}[A-HJ-NP-Z0-9—ßæØ∏€∞ƒ¡Ï]'

@annotate("string,string->string")
class PyHpzl2Hpys(object):
    def evaluate(self, ori_hphm, ori_hpzl):
        """
        Parameters
        ----------
        
        hphm: ∫≈≈∆∫≈¬Î
        hpzl: ∫≈≈∆÷÷¿‡
        
        """
        try:
            if ori_hphm and ori_hpzl:
                hphm = ''.join([chinese.get(v, v) for v in ori_hphm.decode("utf8")]).upper()
                hphm = re.sub(u' ', u'', hphm)
                hpzl = re.sub(u' ', u'', ori_hpzl)
                hpzl = re.sub(u'D', u'0', hpzl)
                hpzl = '02' if hpzl == 'Œﬁ' else hpzl
                hpzl = hpzl if bool(re.match(r'\d+$', hpzl)) else '02'
                hpzl = int(hpzl)
                if hpzl == 1 or hphm[-1] == u'π“':
                    return '01'
                if hphm[-1] in u' π¡Ïπ“—ßæØ∏€∞ƒ':
                    return '00'
                if bool(re.match(NEW_ENERGY_VEHICLE_RE, hphm)):
                    return '03'      
            return '02'
        except:
            raise Exception("±®¥Ì£¨hphm:'%s', hpzl:'%s'" % (ori_hphm, ori_hpzl))
