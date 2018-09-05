# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 00:13
# @Author  : huanghaohao
# @Email   : haohao.huang@easytransfer.cn
# @File    : test2.py
# @Software: PyCharm

import requests
import json
server = 'http://localhost:9200'

def put():
    data = {
      "title": "My first blog entry",
      "text":  "Just trying this out... hhhhhh",
      "date":  "2014/01/01",
      "name": 'huang'
    }
    data = json.dumps(data)
    result = requests.put('http://localhost:9200/website/blog/1', data=data,
                      headers={'Content-Type': 'application/json'})
    return result


def get(search):
    result = requests.get(server + search)
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


def post(data):
    data = json.dumps(data)
    result = requests.post(server + '/website/blog/1/_update', data=data,
                           headers={'Content-Type': 'application/json'})
    return result


if __name__ == '__main__':
    search = '/website/blog/1'
    # result = get(search)
    # result = put()
    data = {
        "script": "ctx._source.tags+=new_tag",
        "params": {
            "new_tag": "search"
        }
    }

    result = post(data)
    # result = put()
    print(json.loads(result.content))