from odps.udf import annotate
from odps.udf import BaseUDTF
@annotate('string ->string,string,string,string,string,string,string,string,string,string,string')
class wbtsw(BaseUDTF):
    def process(self,arg):
        zs_lst = arg.split('^')
        try:
            for i in zs_lst:
                for j in zs_lst:
                    if i == j:
                        continue 
                    i_lst = i.split('|')
                    j_lst = j.split('|')
                    i_sxsj = int(i_lst[4])
                    i_xxsj = int(i_lst[5])
                    j_sxsj = int(j_lst[4])
                    j_xxsj = int(j_lst[5])
                    if abs(i_sxsj - j_sxsj) <= 300 and abs(i_xxsj-j_xxsj) <=300:
                        self.forward(i_lst[0],i_lst[1],i_lst[2],i_lst[3],i_lst[6],j_lst[0],j_lst[1],j_lst[2],j_lst[3],j_lst[7],i_lst[2])
        except:
            pass
