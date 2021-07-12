# s3-to-elasticsearch
Stream data from S3 endpoints to your Elasticsearch

## Run Kibana on Docker to view Elasticsearch data 

To start an Elasticsearch container, run:
```
docker network create elastic
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.13.3
docker run --name es01-test --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.13.3
```
To start Kibana and connect it to your Elasticsearch container, run the following commands in a new terminal session:
```
docker pull docker.elastic.co/kibana/kibana:7.13.3
docker run --name kib01-test --net elastic -p 5601:5601 -e "ELASTICSEARCH_HOSTS=http://es01-test:9200" docker.elastic.co/kibana/kibana:7.13.3
```
To access Kibana, go to http://localhost:5601.


For the script to stream data, we use ``python`` and use the ``cloudpathlib`` which we can use for google-cloud-storage, azure or s3.

```
pip install cloudpathlib
```

https://cloudpathlib.drivendata.org/

For S3, You need to store your aws credentials in the default location ``~/.aws/credentials``



