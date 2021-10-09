# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 17:02
# @Author  : wanghc
# @File    : 1.连接mongodb.py
# @Software: PyCharm

import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client['local']

collection = db['students']

student = {

    'id': '20170101',

    'name': 'Jordan',

    'age': 20,

    'gender': 'male'

}

student1 = {

    'id': '20170101',

    'name': 'HuaSen',

    'age': 20,

    'gender': 'male'

}



student2 = {

    'id': '20170202',

    'name': 'Mike',

    'age': 21,

    'gender': 'male'

}



result = collection.insert_many([student1, student2])

print(result)

print(result.inserted_ids)
