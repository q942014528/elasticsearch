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

    def mget(self, docs, mget_key = ''):
        if mget_key:
            url = "{url}/{index}/{type}/_mget".format(url=self.url, index=self.index, type=self.type)
        else:
            url = "{url}/_mget".format(url=self.url)

        data = json.dumps(docs)
        result = requests.get(url, data=data, headers={'Content-Type': 'application/json'})
        print(result.content)

    def bulk(self, data, bulk_key=False):

        if bulk_key:
            url = "{url}/{index}/{type}/_bulk".format(url=self.url, index=self.index, type=self.type)
        else:
            url = "{url}/_bulk".format(url=self.url)
        data = json.dumps(data)
        result = requests.post(url, data=data, headers={'Content-Type': 'application/json'})
        print(result.content)

    def get_all(self):
        url = "{url}/_search".format(url=self.url)
        result = requests.get(url)
        print(result.content)


if __name__ == '__main__':

    elastic_search = ElasticSearch(sea_index='test', sea_type='blog')

    data = {'name': 'huanghaohao', 'age': 25, 'address': 'beijing'}
    query_info = {
        'query': {
            'match': {
                'name': 'lisi'
            }
        },

    }
    docs = {
        'docs': [
            {'_index': elastic_search.index,
             '_type': elastic_search.type,
             '_id': '3'},
            {'_index': elastic_search.index,
             '_type': elastic_search.type,
             '_id': '4'}
        ]
    }
    docs2 = {
        'ids': ['4', '3', '5']
    }
    sea_index = elastic_search.index
    sea_type = elastic_search.type
    elastic_search.get(id=4)

    bulk_data = """{ "delete": { "_index": """+ sea_index + """, "_type": """ + sea_type+""", "_id": "4" }}\\n"""
    print(bulk_data)
    # elastic_search.head(data=query_info)
    # elastic_search.get()
    # elastic_search.mget(docs2, mget_key=True)
    # elastic_search.bulk(data=bulk_data)
    # elastic_search.get_all()
    # elastic_search.put(data=data, id=4, create=True)
    # elastic_search.delete(id=1)