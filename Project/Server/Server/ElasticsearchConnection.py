import math
import random
import sys
from typing import Dict, List

import configparser

from elastic_transport import ApiResponse
from elasticsearch import Elasticsearch

from Pipeline.Analysis.Util import split_list
from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import GeniusSongs
from Pipeline.Lyrics_Scraping.Song import Song, dict_to_song


class ElasticsearchConnection:
    def __init__(self):
        es_host = "http://localhost:9200"
        [es_user, es_password] = get_es_variables()
        self.es = Elasticsearch(es_host, http_auth=(es_user, es_password))

    def create_index(self, index_name: str, mapping: Dict | None = None) -> None:
        self.es.indices.create(index=index_name, settings=get_analyzer())

    def delete_index(self, index_name: str) -> None:
        res = self.es.indices.delete(index=index_name, ignore=[400, 404])
        print(res)

    def insert_one_data(self, song: Song, index_name: str = "lyrics_data") -> None:
        song.flatten_matching_categories()
        res = self.es.index(index=index_name, id=song.genius_track_id, document=song.__dict__)
        print(res)

    def insert_bulk(self, songs: GeniusSongs, index_name: str = "lyrics_data") -> None:
        for song in songs.song_list:
            song.flatten_matching_categories()

        for chunk_list in split_list(songs.song_list, 10):
            res = self.es.bulk(index=index_name, operations=generate_docs(chunk_list, index_name))
        print(res)

    def delete_all_entries(self, index_name: str = "lyrics_data") -> None:
        self.es.delete_by_query(index=index_name, query={"match_all": {}})

    def get_by_id(self, track_id: int, index_name: str = "lyrics_data") -> None | Song:
        res = self.es.search(index=index_name,
                             query={"ids": {"values": [track_id]}})

        try:
            temp_song = get_list_from_api_response(res)[0]
            return temp_song[0]
        except:
            return None

    def search_for_song_and_artist(self, search_word: str, index_name: str = "lyrics_data") -> None | List[Song]:
        res = self.es.search(index=index_name,
                             query={"multi_match": {
                                 "query": search_word,
                                 "fields": ["title^3", "lyrics", "artist_name^3", "writer_artist^3"]
                             }})

        try:
            return get_list_from_api_response(res)
        except:
            return None

    def get_by_artist_id(self, artist_id: int, index_name: str = "lyrics_data") -> None | Song:
        res = self.es.search(index=index_name,
                             query={"bool": {"filter": {"term": {"artist_id": artist_id}}}})

        try:
            temp_song = get_list_from_api_response(res)
            return temp_song
        except:
            return None

    def get_random_song(self, index_name: str = "lyrics_data"):
        res = self.es.search(index=index_name,
                             size=1,
                             query={
                                 "function_score": {
                                     "functions": [
                                         {
                                             "random_score": {
                                                 "seed": random.Random().randint(0, 100000)
                                             }
                                         }
                                     ]
                                 }})
        try:
            temp_song = get_list_from_api_response(res)[0]
            return temp_song[0]
        except:
            return None


def get_list_from_api_response(response: ApiResponse):
    temp = response['hits']['hits']
    return list(map(lambda song: (dict_to_song(song['_source']), song['_score']), temp))


def generate_docs(song_list: List[Song], index_name: str = "lyrics_data"):
    actions = []
    for song in song_list:
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
