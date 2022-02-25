# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 17:53:08 2021
�������� ת ������ɫ
@author: 18768191466
"""
from odps.udf import annotate
import re

chinese = {
    u'һ': u'1',
    u'��': u'2',
    u'��': u'3',
    u'��': u'4',
    u'��': u'5',
    u'��': u'6',
    u'��': u'7',
    u'��': u'8',
    u'��': u'9',
    u'��': u'1',
    u'��': u'7',
    u'��': u'0',
    u'��': u'2',
    u'��': u'9'
}
# 97ʽ�����Ƹ�ʽ
MILITARY_VEHICLES = u'[���ұ���������������δ��][A-Z]\d{5}'
MILITARY_VEHICLES_TWO = u'[���������Ϲ�ɺ��վ�][A-Z]\d{5}'
# 13ʽ�侯����
ARMED_POLICE_VEHICLE = u'WJ[�����弽ԥ���ɺ�����³������Ӷ���ʽ����¼���������ش�����]\d{4}[XBTSGJD]'
# �¾�������
NEW_MILITARY_VEHICLES = u'[ABCGNJLSHK][A-Z]\d{5}'
# ���ó���
ORDINARY_CAR_RE = u'[�����弽ԥ���ɺ�����³������Ӷ���ʽ����¼���������ش�����ʹ��][A-Z][A-HJ-NP-Z0-9]{4}[A-HJ-NP-Z0-9��ѧ���۰�]'
# ����Դ����
NEW_ENERGY_VEHICLE_RE = u'[�����弽ԥ���ɺ�����³������Ӷ���ʽ����¼���������ش�����ʹ��][A-Z](([0-9]{5}[DF])|([DF][A-HJ-NP-Z0-9][0-9]{4}))'
# ũ�ó���
CIVIL_CAR_ONE = u'[���ʸ�����վ�ԥ�ڼ����Ƽ���³�����ɽ��������������²ش�������][0-5][0-9]\d{5}'
CIVIL_CAR_TWO = u'(����|����|����|����|������|����|����|����|�㶫|����|�ӱ�|����|ɽ��|�Ĵ�|����|�½�|����|����|����|�Ϻ�|���|���ɹ�|����|ɽ��|����|����|�ຣ|����|����|�㽭|����)[A-Z]\d{5}'
CIVIL_CAR = CIVIL_CAR_ONE + '|' + CIVIL_CAR_TWO
# Ħ�г���
MOBILE_RE = u'[�����弽ԥ���ɺ�����³������Ӷ���ʽ����¼���������ش�����ѧʹ�쾯][A-Z][A-HJ-NP-Z0-9]{3}[A-HJ-NP-Z0-9ѧ���۰���]'

@annotate("string,string->string")
class PyHpzl2Hpys(object):
    def evaluate(self, ori_hphm, ori_hpzl):
        """
        Parameters
        ----------
        
        hphm: ���ƺ���
        hpzl: ��������
        
        """
        try:
            if ori_hphm and ori_hpzl:
                hphm = ''.join([chinese.get(v, v) for v in ori_hphm.decode("utf8")]).upper()
                hphm = re.sub(u' ', u'', hphm)
                hpzl = re.sub(u' ', u'', ori_hpzl)
                hpzl = re.sub(u'D', u'0', hpzl)
                hpzl = '02' if hpzl == '��' else hpzl
                hpzl = hpzl if bool(re.match(r'\d+$', hpzl)) else '02'
                hpzl = int(hpzl)
                if hpzl == 1 or hphm[-1] == u'��':
                    return '01'
                if hphm[-1] in u'ʹ���ѧ���۰�':
                    return '00'
                if bool(re.match(NEW_ENERGY_VEHICLE_RE, hphm)):
                    return '03'      
            return '02'
        except:
            raise Exception("����hphm:'%s', hpzl:'%s'" % (ori_hphm, ori_hpzl))
