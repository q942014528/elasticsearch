# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 00:13
# @Author  : huanghaohao
# @Email   : haohao.huang@easytransfer.cn
# @File    : test2.py
# @Software: PyCharm

import requests
import json


def put():
    data = {
      "title": "My first blog entry",
      "text":  "Just trying this out... hhhhhh",
      "date":  "2014/01/01",
      "name": 'huang'
    }
    data = json.dumps(data)
    result = requests.put('http://localhost:9200/website/blog/123', data=data,
                      headers={'Content-Type': 'application/json'})
    return result


def get(search):
    result = requests.get('http://localhost:9200' + search)
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


if __name__ == '__main__':
    search = '/website/blog/123'
    result = get(search)
    # result = put()
    # result = post()
    print(json.loads(result.content))