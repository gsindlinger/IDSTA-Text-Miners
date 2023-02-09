import json
import os
from typing import List, Dict, Tuple

import gensim
from gensim.models import Word2Vec, KeyedVectors
from tqdm import *
import requests

from Pipeline.Analysis import Util

URL_WORD_2_VEC_MODEL_GERMAN = "https://cloud.devmount.de/d2bc5672c523b086/german.model"
MODEL_PATH = "data/word2vec_german.model"


class CategoryDictionary:

    def __init__(self, should_load_model: bool | None = True):
        self.categories: Dict[str, Tuple[str, str]] = {}
        if should_load_model:
            load_word_2_vec_from_web()
            # load word2vec model from https://devmount.github.io/GermanWordEmbeddings/
            self.word2vec_model: KeyedVectors | None = gensim.models.KeyedVectors.load_word2vec_format(MODEL_PATH, binary=True)


    def add_new_members_to_category(self, category: str,
                                    positive_search_words: str | None = None,
                                    negative_search_words: str | None = None,
                                    items: int = 20) -> None:
        positive_search_word_list = [x.strip() for x in positive_search_words.split(',')] \
            if positive_search_words \
            else [category]
        # positive_search_word_list.extend([x.title() for x in positive_search_word_list[:]])
        negative_search_word_list = [x.strip() for x in negative_search_words.split(',')] \
            if negative_search_words \
            else []
        # negative_search_word_list.extend([x.title() for x in negative_search_word_list[:]])

        # filter out words which don't appear in the corpus of the given model
        search_word_list_filtered = [[], []]
        for i, word_list in enumerate([positive_search_word_list, negative_search_word_list]):
            for word in word_list:
                if word in self.word2vec_model:
                    search_word_list_filtered[i].append(word)
                else:
                    print(f"Search word could not be detected in the given model and will be ignored: {word}")

        top_similar: List[Tuple[str, float]] = self.word2vec_model.most_similar(positive=search_word_list_filtered[0],
                                                                                negative=search_word_list_filtered[1],
                                                                                topn=items)

        # filter for items which have a low similarity
        top_similar = list(filter(lambda word_tuple: word_tuple[1] > 0.3, top_similar))
        # filter for items which don't contain of multiple words like 'schwul_lesbisch'
        top_similar = list(filter(lambda word_tuple: "_" not in word_tuple[0], top_similar))

        positive_search_word_list.extend(list(map(lambda x: x[0], top_similar)))
        positive_search_word_list_lemmatized = list(map(lambda term: Util.lemmatize(term)[0], positive_search_word_list))

        positive_search_words_dict = build_original_lemmatized_dict(positive_search_word_list,
                                                                    positive_search_word_list_lemmatized)

        self.categories.update({category: positive_search_words_dict})

    def build_dictionary_model(self):
        item_size = 20
        positive_search_words_homophopic = "Schwuchtel, Homo, homo, trans, Transe, schwul, gay, lesbisch, Lesbe"
        negative_search_words_homophobic = "Fotze, hetero, Neger"
        self.add_new_members_to_category(category="Homophobie",
                                         positive_search_words=positive_search_words_homophopic,
                                         negative_search_words=negative_search_words_homophobic,
                                         items=item_size)

        positive_search_words_misogynistic = "Pussy, Bitch, Schlampe, Hure, Nutte, Fotze, " \
                                             "ficken, Titten, Sex, Jungfrau, kochen, Vergewaltigung"
        negative_search_words_misogynistic = "Nigger, Schwuchtel"
        self.add_new_members_to_category(category="Frauenfeindlichkeit",
                                         positive_search_words=positive_search_words_misogynistic,
                                         negative_search_words=negative_search_words_misogynistic,
                                         items=item_size)

        positive_search_words_anti_disabled = "behindert, Mongo, Krueppel, Spast, Spacko, Spasti, Rollstuhl"
        negative_search_words_anti_disabled = "schwul, Fotze"
        self.add_new_members_to_category(category="Behindertenfeindlichkeit",
                                         positive_search_words=positive_search_words_anti_disabled,
                                         negative_search_words=negative_search_words_anti_disabled,
                                         items=item_size)

        positive_search_words_antisemitic = "Jude, KZ, Juedin, Israel, Judas, Holocaust"
        negative_search_words_antisemitic = "schwul, Fotze, Neger"
        self.add_new_members_to_category(category="Antisemitismus",
                                         positive_search_words=positive_search_words_antisemitic,
                                         negative_search_words=negative_search_words_antisemitic,
                                         items=item_size)

        positive_search_words_racist = "Nigga, Neger, Assi, schwarz, Sklave, Stern"
        negative_search_words_racist = "schwul, Fotze, behindert, weiss"
        self.add_new_members_to_category(category="Rassismus",
                                         positive_search_words=positive_search_words_racist,
                                         negative_search_words=negative_search_words_racist,
                                         items=item_size)

        positive_search_words_violence = "schlagen, tot, Idiot, fuck, verrecken"
        self.add_new_members_to_category(category="Gewalt",
                                         positive_search_words=positive_search_words_violence,
                                         items=item_size)

        positive_search_words_love = "Liebe, Freunde, zusammen, Liebeslied, Freundin"
        self.add_new_members_to_category(category="Liebe",
                                         positive_search_words=positive_search_words_love,
                                         items=item_size)

        positive_search_words_sadness = "traurig, zerreissen, Kummer"
        negative_search_words_sadness = "gluecklich"
        self.add_new_members_to_category(category="Trauer",
                                         positive_search_words=positive_search_words_sadness,
                                         negative_search_words=negative_search_words_sadness,
                                         items=item_size)

        self.to_json("data/categories.json")

    def __str__(self):
        return json.dumps(self.categories, sort_keys=True, indent=4)

    def to_json(self, filename):
        json_string = json.dumps(self.categories, sort_keys=True, indent=4)
        with open(filename, 'w', encoding='utf8') as f:
            f.write(json_string)


def read_from_json(filename: str) -> CategoryDictionary:
    categories = CategoryDictionary(should_load_model=False)
    with open(filename, 'r') as f:
        json_data = f.read()

    dict_values = json.loads(json_data)
    # flatten the dictionary
    # songs.song_list = [item for sublist in [list(songs.values()) for songs in dict_values] for item in sublist]
    categories.categories = {category: list(map(lambda x: tuple(x), value_list)) for category, value_list in json.loads(json_data).items()}
    return categories


def build_original_lemmatized_dict(list1: List[str], list2: List[str]):
    filtered_zip: List[Tuple[str, str]] = list(map(lambda x: (x[0], x[0]) if '--' in x[1] else x,
                                                   list(zip(list1, list2))))
    filtered_zip = list(map(lambda x: (x[0], x[1].lower()), filtered_zip))
    return filtered_zip


def load_word_2_vec_from_web():
    if not os.path.exists(MODEL_PATH):
        with requests.get(URL_WORD_2_VEC_MODEL_GERMAN, stream=True) as r:
            r.raise_for_status()
            with open(MODEL_PATH, 'wb') as f:
                pbar = tqdm(total=int(r.headers['Content-Length']))
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        pbar.update(len(chunk))
