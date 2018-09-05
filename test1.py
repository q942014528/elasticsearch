# -*- coding: utf-8 -*-
# @Time    : 2018/9/2 13:50
# @Author  : huanghaohao
# @Email   : haohao.huang@easytransfer.cn
# @File    : test1.py
# @Software: PyCharm

import requests
import json


def put():
    data = {
        "first_name": "Douglas",
        "last_name": "Fir",
        "age": 35,
        "about": "I like to build cabinets",
        "interests": ["forestry"]
    }
    data = json.dumps(data)
    result = requests.put('http://localhost:9200/megacorp/employee/3', data=data,
                      headers={'Content-Type': 'application/json'})
    return result


def get(search):
    result = requests.get('http://localhost:9200' + search + '&pretty')
    return result

def dsl_get():
    data = {
            "query" : {
                "match_phrase" : {
                    "about" : "rock climbing"
                }
            },
            "highlight": {
                "fields" : {
                    "about" : {}
                }
            }
        }




    data = json.dumps(data)
    result = requests.get('http://localhost:9200/megacorp/employee/_search', data=data,
                          headers={'Content-Type': 'application/json'})
    return result

def post():
    data = [{ "index": { "_id": 1 }},
            { "price" : 10, "productID" : "XHDK-A-1293-#fJ3" },
            { "index": { "_id": 2 }},
            { "price" : 20, "productID" : "KDKE-B-9947-#kL5" },
            { "index": { "_id": 3 }},
            { "price" : 30, "productID" : "JODL-X-1937-#pV7" },
            { "index": { "_id": 4 }},
            { "price" : 30, "productID" : "QQPX-R-3956-#aD8" }]
    data_json = ''
    for i in range(len(data)):
        data_json += json.dumps(data[i])
        if i % 2 == 1:
            data_json += '\n'
    result = requests.post('http://localhost:9200/my_store/products/_bulk', data=data_json,
                           headers={'Content-Type': 'application/json'})
    return result

if __name__ == '__main__':
    # search = '/megacorp/employee/_search?q=last_name:Smith'
    search = '/my_store/products/_search'
    # result = get(search)
    # result = dsl_get()
    result = post()
    print(json.loads(result.content))