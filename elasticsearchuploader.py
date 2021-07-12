from pprint import pprint
import requests
import urllib
import json
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from elasticsearch.serializer import JSONSerializer
import os,sys

directory = 'output.json'   #json-file-to-upload

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

with open(directory, 'r', encoding='utf-8') as f:
    data=json.loads(f.read())
pprint(data)

es.index(index='jsonindex', doc_type='doc', body=data)
