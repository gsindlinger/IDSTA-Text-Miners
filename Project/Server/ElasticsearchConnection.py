from typing import Dict, List

import configparser
from elasticsearch import Elasticsearch


class ElasticsearchConnection:
    def __init__(self):
        es_host = "http://localhost:9200"
        [es_user, es_password] = get_es_variables()
        self.es = Elasticsearch(es_host, http_auth=(es_user, es_password))

    def create_index(self, index_name: str, mapping: Dict) -> None:
        self.es.indices.create(index=index_name, ignore=400, body=mapping)
        self.es.indices.close(index=index_name)
        self.es.indices.put_settings(index=index_name, body=get_analyzer())
        self.es.indices.open(index=index_name)


def get_analyzer() -> Dict:
    return {"analysis":
        {"analyzer": {
            "default": {
                "type": "german"
            }
        }}}


def get_es_variables() -> List[str]:
    config = configparser.ConfigParser()
    config.read("../env/elasticsearch.env")
    es_user = config["DEFAULT"]["ELASTIC_USERNAME"]
    es_password = config["DEFAULT"]["ELASTIC_PASSWORD"]
    return [es_user, es_password]
