# Code to work with elasticsearch python library
from elasticsearch import Elasticsearch

if __name__ == '__main__':
    print('Hello World')
    es = Elasticsearch()
    index_mapping_body = {
       "mappings": {
           "properties": {
               "age":    { "type": "integer" },
               "email":  { "type": "keyword"  },
               "name":   { "type": "text"  }
           }
       }
    }
    create_response = es.indices.create(index='test-index-with-mapping',body=index_mapping_body)
    print(create_response)
    response = es.indices.exists(index='test-index')
    print(response)
