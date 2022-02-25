from odps.udf import annotate
from odps.udf import BaseUDTF
'''
火车同通道  UDTF
'''
@annotate('string ->string,string,string,string,string,string,string,string,string,string,string,string,string,string')
class hcttd(BaseUDTF):
    def process(self,arg):
        zs_lst = arg.split('^')
        try:
            for i in zs_lst:
                for j in zs_lst:
                    if i == j:
                        continue 
                    i_lst = i.split('|')
                    j_lst = j.split('|')
                    i_jpsj_int = int(i_lst[2])
                    j_jpsj_int = int(j_lst[2])
                    if abs(i_jpsj_int - j_jpsj_int) <= 30:
                        self.forward(i_lst[0],i_lst[1],i_lst[3],i_lst[4],i_lst[5],i_lst[6],i_lst[7],i_lst[8],j_lst[3],j_lst[4],j_lst[5],j_lst[6],j_lst[7],j_lst[8])
        except:
            pass


