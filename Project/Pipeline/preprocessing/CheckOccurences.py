import concurrent
import itertools
from collections import Counter
from typing import Tuple, Dict, List

import pandas as pd
from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import GeniusSongs
from Pipeline.Lyrics_Scraping.Song import Song
from Pipeline.preprocessing.CategoryDictionary import CategoryDictionary, read_from_json
import Util
from tqdm import *


categories: CategoryDictionary = read_from_json("data/categories.json")


def check_occurences_songs(songs: GeniusSongs) -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        list(tqdm(executor.map(check_occurences_song, songs.song_list), total=len(songs.song_list)))



def check_occurences_song(song: Song) -> None:
    preprocessed_lyrics = song.lyrics
    preprocessed_lyrics = Util.remove_stopwords_and_punctuation(preprocessed_lyrics)
    preprocessed_lyrics = Util.remove_trash_words(preprocessed_lyrics)
    preprocessed_lyrics = Util.remove_symbols(preprocessed_lyrics)
    preprocessed_lyrics, word_mapping = Util.lemmatize(preprocessed_lyrics)
    word_mapping = Util.reverse_dict(word_mapping)

    for category, category_values in categories.categories.items():
        check_against_category(preprocessed_lyrics, word_mapping, song, category, category_values)


def check_against_category(preprocessed_lyrics_temp: str, word_mapping: Dict[str, List[str]], song_temp: Song, category: str, category_values: Tuple[str, str]):
    if song_temp.matched_categories is None:
        song_temp.matched_categories = {}
    counted_words = Counter(preprocessed_lyrics_temp.split())
    for word, count in counted_words.most_common():
        if word in list(map(lambda x: x[1], category_values)):
            if category in song_temp.matched_categories:
                song_temp.matched_categories[category].append((word, count, word_mapping[word]))
            else:
                song_temp.matched_categories[category] = [(word, count, word_mapping[word])]


def sum_occurences_over_time(songs_dict) -> pd.DataFrame:
    columns = [str(i) for i in range(1998, 2024)]
    index = list(categories.categories.keys())
    results = pd.DataFrame(0,
                           index=index,
                           columns=columns)
    for song in songs_dict.song_list:
        year = song.release_date[0:4]
        for category, matched_word_list in song.matched_categories.items():
            results.at[category, year] = results.at[category, year] + matched_word_list[1]

    return results


