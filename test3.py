# -*- coding: utf-8 -*-
# @File      : test3.py

import requests
import json

bulk_data = [
            { "index": { "_id": 1 }},
            { "title": "The quick brown fox" },
            { "index": { "_id": 2 }},
            { "title": "The quick brown fox jumps over the lazy dog" },
            { "index": { "_id": 3 }},
            { "title": "The quick brown fox jumps over the quick dog" },
            { "index": { "_id": 4 }},
            { "title": "Brown fox brown dog" }
            ]
new_bulk_data = ""


for i in bulk_data:
    data = json.dumps(i)
    new_bulk_data += data + '\n'

# result = requests.post('http://localhost:9200/my_index/my_type/_bulk', data=new_bulk_data, headers={'Content-Type': 'application/json'})

query_data = {'query': {
                    "match": {
                        "title": {
                            'query': 'The quick brown fox',
                        }
                    }
                }
             }

bool_data = {
  "query": {
    "bool": {
      "must":     { "match": { "title": "quick" }},
      "must_not": { "match": { "title": "lazy"  }},
      "should": [
                  { "match": { "title": "brown" }},
                  { "match": { "title": "dog"   }}
      ]
    }
  }
}

update = {
    "my_type": {
        "properties": {
            "english_title": {
                "type":     "text",
                "analyzer": "english"
            }
        }
    }
}


query_data = json.dumps(query_data)
# update = json.dumps(update)

result = requests.get('http://localhost:9200/my_index/my_type/_search?search_type=dfs_query_then_fetch', data=query_data, headers={'Content-Type': 'application/json'})
# result = requests.get('http://localhost:9200/my_index/my_type/_mapping', data=query_data, headers={'Content-Type': 'application/json'})
# result = requests.put('http://localhost:9200/my_index/_mapping/my_type', data=update, headers={'Content-Type': 'application/json'})

print(result.content)