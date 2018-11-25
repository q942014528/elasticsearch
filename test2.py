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
      "text":  "Just trying this out... hhhhhh22212321312",
      "date":  "2014/01/02",
      "name": 'huanghaohao'
    }
    data = json.dumps(data)
    result = requests.put('http://localhost:9200/megacorp/employee/2', data=data,
                      headers={'Content-Type': 'application/json'})
    return result


def get(search):
    result = requests.get(server + search)
    return result


def dsl_get():
    data = {
            "query" : {
                "match_phrase" : {
                    "text" : "hhhhhh"
                }
            },
        }

    data = json.dumps(data)
    result = requests.get('http://localhost:9200/website/blog/_search', data=data,
                          headers={'Content-Type': 'application/json'})
    return result


def post(data):
    data = json.dumps(data)
    result = requests.post(server + '/website/blog/1/_update', data=data,
                           headers={'Content-Type': 'application/json'})
    return result


def delete(id):
    result = requests.delete(f'http://localhost:9200/website/blog/{id}',
                          headers={'Content-Type': 'application/json'})
    return result


if __name__ == '__main__':
    search = '/website/blog/1'
    # result = get(search)
    # result = put()
    # result = dsl_get()
    result = delete(1)
    data = {
        "script": "ctx._source.tags+=new_tag",
        "params": {
            "new_tag": "search"
        }
    }

    # result = post(data)
    # result = put()
    print(json.loads(result.content))