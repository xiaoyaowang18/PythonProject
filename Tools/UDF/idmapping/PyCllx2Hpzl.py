# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 14:12:28 2021
�ӡ��������͡� �� ������������������롱 ����ת��
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
class PyCllx2Hpzl(object):
    def evaluate(self, hphm, cllx):
        """
        Parameters
        ----------
        
        hphm: ���ƺ���
        cllx: ��������
        
        """
        if hphm and cllx:
            hphm = ''.join([chinese.get(v, v) for v in hphm.decode("utf8")]).upper()
            hphm = re.sub(r' ', '', hphm)
            cllx = int(cllx)
            # Ħ�г�
            if bool(re.match(MOBILE_RE, hphm)):
                if hphm[0] == 'ʹ':
                    return '09'	#  ʹ��Ħ�г�
                elif  hphm[-1] == '��':
                    return '10'	#  ���Ħ�г�
                elif hphm[-1] == 'ѧ':
                    return '17'	#  ����Ħ�г�
                elif hphm[-1] == '��':
                    return '24'  #	����Ħ��
                else: #��������Ħ�г����͵ĳ��� �޷��ж�
                    return '07'	#  ��ͨĦ�г�
            # ������
            else:
                if hphm[0] == 'ʹ':
                    return '03'	#  ʹ������
                elif  hphm[-1] == '��':
                    return '04'   #	�������
                if bool(re.match(MILITARY_VEHICLES, hphm)) or\
                bool(re.match(NEW_MILITARY_VEHICLES, hphm)) or\
                bool(re.match(MILITARY_VEHICLES_TWO, hphm)):
                    return '32'	    #  ���Ӻ���
                if bool(re.match(ARMED_POLICE_VEHICLE, hphm)):
                    return '31'      #	�侯����
                if bool(re.match(ORDINARY_CAR_RE, hphm)):
                    if  hphm[-1] == '��':
                        return '15	'#  �ҳ�
                    elif hphm[-1] == 'ѧ':
                        return '16'	#  ��������
                    elif hphm[-1] == '��':
                        return '23'	#  ��������
                    elif hphm[-1] == '��':
                        return '26'	#  ����������
                    elif hphm[-1] == '��':
                        return '27'	#  �����������
                if bool(re.match(CIVIL_CAR, hphm)):
                    return '25'      # 	ԭũ������
                # �ͳ�����������ͳ�������������ͳ������ͳ����аͳ�
                if cllx in (3, 2, 16, 17, 2, 15):
                    if bool(re.match(NEW_ENERGY_VEHICLE_RE, hphm)):
                        return '51'	#  ��������Դ����
                    return '01'   #	��������
                # �γ���suv��С�����������
                if cllx in (1, 11, 12, 14, 13):
                    if bool(re.match(NEW_ENERGY_VEHICLE_RE, hphm)):
                        return '52'	#  С������Դ����
                    return '02'   #	��������                    
        return '99'
            