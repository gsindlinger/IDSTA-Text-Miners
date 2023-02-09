import random
from typing import Dict, List

import configparser

from elastic_transport import ApiResponse
from elasticsearch import Elasticsearch

from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import GeniusSongs
from Pipeline.Lyrics_Scraping.Song import Song, dict_to_song


class ElasticsearchConnection:
    def __init__(self):
        es_host = "http://localhost:9200"
        [es_user, es_password] = get_es_variables()
        self.es = Elasticsearch(es_host, http_auth=(es_user, es_password))

    def create_index(self, index_name: str, mapping: Dict) -> None:
        self.es.indices.create(index=index_name, mappings=mapping, settings=get_analyzer())

    def delete_index(self, index_name: str) -> None:
        res = self.es.indices.delete(index=index_name, ignore=[400, 404])
        print(res)

    def insert_one_data(self, index_name: str, song: Song) -> None:
        res = self.es.index(index=index_name, id=song.genius_track_id, document=song.__dict__)
        print(res)

    def insert_bulk(self, index_name: str, songs: GeniusSongs) -> None:
        res = self.es.bulk(index=index_name, operations=generate_docs(index_name, songs))
        print(res)

    def delete_all_entries(self, index_name: str) -> None:
        self.es.delete_by_query(index=index_name, query={"match_all": {}})

    def get_by_id(self, index_name: str, track_id: int) -> None | Song:
        res = self.es.search(index=index_name,
                             query={"ids": {"values": [track_id]}})

        try:
            temp_song = get_list_from_api_response(res)[0]
            return temp_song[0]
        except:
            return None

    def search_in_title_and_lyrics(self, index_name: str, search_word: str) -> None | List[Song]:
        res = self.es.search(index=index_name,
                             query={"multi_match": {
                                 "query": search_word,
                                 "fields": ["title^3", "lyrics"]
                             }})

        try:
            return get_list_from_api_response(res)
        except:
            return None

    def get_by_artist_id(self, index_name: str, artist_id: int) -> None | Song:
        res = self.es.search(index=index_name,
                             query={"bool": {"filter": {"term": {"artist_id": artist_id}}}})

        try:
            temp_song = get_list_from_api_response(res)
            return temp_song
        except:
            return None

    def get_random_song(self, index_name: str):
        res = self.es.search(index=index_name,
                             size=1,
                             query={
                                 "function_score": {
                                     "functions": [
                                         {
                                             "random_score": {
                                                 "seed": random.Random().randint()
                                             }
                                         }
                                     ]
                                 }})


def get_list_from_api_response(response: ApiResponse):
    temp = response['hits']['hits']
    return list(map(lambda song: (dict_to_song(song['_source']), song['_score']), temp))


def generate_docs(index_name: str, songs: GeniusSongs):
    actions = []
    for song in songs.song_list:
        action = {"index": {"_index": index_name, "_id": song.genius_track_id}}
        actions.append(action)
        actions.append(song.__dict__)
    return actions


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
