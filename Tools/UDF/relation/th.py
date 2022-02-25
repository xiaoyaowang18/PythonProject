from odps.udf import annotate
from odps.udf import BaseUDTF
@annotate('string ->string,string,string,string,string,string,string,string,string')
class th(BaseUDTF):
    def process(self,arg):
        zs_lst = arg.split('^')
        try:
            for i in zs_lst:
                for j in zs_lst:
                    if i == j:
                        continue 
                    i_lst = i.split('|')
                    j_lst = j.split('|')
                    self.forward(i_lst[0],i_lst[1],i_lst[2],i_lst[3],j_lst[1],j_lst[2],j_lst[3],j_lst[5],i_lst[3])
        except:
            pass