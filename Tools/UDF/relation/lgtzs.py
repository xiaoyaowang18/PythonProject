from odps.udf import annotate
from odps.udf import BaseUDTF
'''
旅馆同住宿  UDTF
'''

@annotate('string ->string,string,string,string,string,string,string,string,string,string')
class lgtzs(BaseUDTF):
    def process(self,arg):
        zs_lst = arg.split('^')
        try:
            for i in zs_lst:
                for j in zs_lst:
                    if i == j:
                        continue 
                    i_lst = i.split('|')
                    j_lst = j.split('|')
                    i_rzsj = int(i_lst[9])
                    i_ldsj = int(i_lst[10])
                    j_rzsj = int(j_lst[9])
                    j_ldsj = int(j_lst[10])
                    if abs(i_rzsj - j_rzsj) <= 300 and abs(i_ldsj-j_ldsj) <=300:
                        self.forward(i_lst[2],i_lst[6],i_lst[0],i_lst[8],i_lst[4],i_lst[5],i_lst[3],j_lst[2],j_lst[4],j_lst[5])
        except:
            pass
