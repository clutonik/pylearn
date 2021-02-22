# Code to work with elasticsearch python library
from elasticsearch import Elasticsearch


def create_index(*args, **kwargs):
    print(args)
    print(kwargs)
    #self.index_name = name
    #self.index_mapping_body = body


def create_mapping_body(**kwargs):
    mapping_body = {"mappings": {"properties": {}}}
    for field in kwargs:
        if field not in mapping_body["mappings"]["properties"].keys():
            mapping_body["mappings"]["properties"][field] = {
                "type": kwargs.get(field)
            }

    return mapping_body


if __name__ == '__main__':
    es = Elasticsearch()

    mapping_body = create_mapping_body(age="integer",
                                       email="keyword",
                                       name="text")

    create_response = es.indices.create(index='test-index-with-mapping-2',
                                        body=mapping_body,
                                        ignore=400)
    print(create_response)
