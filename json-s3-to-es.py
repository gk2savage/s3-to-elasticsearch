from pprint import pprint
import requests
import urllib
from cloudpathlib import CloudPath
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from elasticsearch.serializer import JSONSerializer
import json
import sys
import os
#py .\json-s3-to-es.py <file-directory-inside-bucket> <index-for-elasticsearch>         i.e Arguments for script
#py .\json-s3-to-es.py json-stream-data jsonindex

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

print(sys.argv[1])  #file-directory-inside-bucket to download
print(sys.argv[2])  #index for elastisearch

cp = CloudPath("s3://root-directory/"+sys.argv[1])

#Uploading Multi-line json-data in Bulk
for f in cp.glob('**/*'):
    print("\n")
    #print(f)   #Print all files inside bucket
    if '.json' in str(f):   
        print(f.read_text())
        file_data = f.read_text()
        data = json.loads(file_data)
        length = len(data)
        #print(length)    #Print length of Json objects inside data
        for i in range(length):
            print(data[i])
            edata=json.loads(str(data[i]))           
            pprint(edata)
            es.index(index=sys.argv[2], doc_type='doc', body=edata)



