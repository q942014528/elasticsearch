# -*- codeing: utf-8 -*-
# @File      : blog.py
import requests
import json


class ElasticSearch(object):

    def __init__(self, sea_index, sea_type):
        self.index = sea_index
        self.type = sea_type
        self.url = 'http://localhost:9200'

    def put(self, id, data, create=''):
        url = "{url}/{index}/{type}/{id}".format(url=self.url, index=self.index, type=self.type, id=id)
        try:
            data = json.dumps(data)
        except Exception as e:
            print(e)
            return False
        if create:
            url += '?op_type=create'
        result = requests.put(url=url, data=data, headers={'Content-Type': 'application/json'})
        text = json.loads(result.text)
        if text.get('_id'):
            print(text)
        else:
            print('error', text)

    def post(self, data):
        url = "{url}/{index}/{type}".format(url=self.url, index=self.index, type=self.type)
        try:
            data = json.dumps(data)
        except Exception as e:
            print(e)
            return False
        result = requests.post(url=url, data=data, headers={'Content-Type': 'application/json'})
        text = json.loads(result.text)
        if text.get('_id'):
            print(text)
        else:
            print('error', text)

    def get(self, id='', data='', source=''):
        if id:
            url = "{url}/{index}/{type}/{id}".format(url=self.url, index=self.index, type=self.type, id=id)
        else:
            url = "{url}/{index}/{type}/_search".format(url=self.url, index=self.index, type=self.type)
        if not data:
            data = {}
        if source:
            url += '?_source=' + source

        data = json.dumps(data)
        result = requests.get(url=url, data=data, headers={'Content-Type': 'application/json'})
        content = json.loads(result.content)
        print(content)

    def dsl_get(self):
        pass

    def head(self, id='', data=''):
        if id:
            url = "{url}/{index}/{type}/{id}".format(url=self.url, index=self.index, type=self.type, id=id)
        else:
            url = "{url}/{index}/{type}/_search".format(url=self.url, index=self.index, type=self.type)

        if not data:
            data = {}
        result = requests.head(url, data=data)
        print(result.status_code)

    def delete(self, id):
        if id:
            url = "{url}/{index}/{type}/{id}".format(url=self.url, index=self.index, type=self.type, id=id)

        result = requests.delete(url)
        content = json.loads(result.content)
        print(content)
        print(result.status_code)


data = {'name': 'zhangsan', 'age': 21, 'zddress': 'beijing'}
query_info = {
    'query': {
        'match': {
            'name': 'lisi'
        }
    },

}

elastic_search = ElasticSearch(sea_index='test', sea_type='blog')
# elastic_search.head(data=query_info)
# elastic_search.get()
# elastic_search.put(data=data, id=2, create=True)
elastic_search.delete(id=1)