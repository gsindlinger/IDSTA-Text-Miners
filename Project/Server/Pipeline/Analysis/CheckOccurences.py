import concurrent
from collections import Counter, defaultdict
from typing import Tuple, Dict, List

import pandas as pd
from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import GeniusSongs
from Pipeline.Lyrics_Scraping.Song import Song
from Pipeline.Analysis.CategoryDictionary import CategoryDictionary, read_from_json
import Util
from tqdm import *

categories: CategoryDictionary = read_from_json("data/categories.json")
lemmatized_categories: Dict[str, List[str]] = defaultdict()


def check_occurences_songs(songs: GeniusSongs) -> None:
    """
    Multithreaded method which counts the occurrences of words in all given categories
    from the given category dictionary (static file given above). Updates each song
    with the occurrence.

    @param songs:
    @return:
    """

    print("start lemmatizing categories")
    for category, values in tqdm(categories.categories.items()):
        # lemmatized_categories[category] = [term.lower() for term in values]
        lemmatized_categories[category] = [lemmatize_filtered(term).lower().strip() for term in values if term]

    print("start checking occurences of categories")

    for song in tqdm(songs.song_list):
        song.matched_categories = None
        check_occurences_song_already_lemmatized(song)

    # with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    #   list(tqdm(executor.map(check_occurences_song_already_lemmatized, songs.song_list), total=len(songs.song_list)))


def lemmatize_filtered(term: str) -> str:
    lemmatize_helper = Util.lemmatize(term)[0]
    return lemmatize_helper if lemmatize_helper not in ["", "--"] else term


def check_occurences_song_already_lemmatized(song: Song) -> None:
    for category, category_values in lemmatized_categories.items():
        preprocessed_lyrics = "".join(song.processed_lyrics_text)
        '''
        preprocessed_lyrics = Util.remove_stopwords_and_punctuation(preprocessed_lyrics)
        preprocessed_lyrics = Util.remove_trash_words(preprocessed_lyrics)
        preprocessed_lyrics = Util.remove_symbols(preprocessed_lyrics)
        '''
        check_against_category_without_mapping(preprocessed_lyrics.lower().strip(), song, category, category_values)


def check_occurences_song(song: Song) -> None:
    preprocessed_lyrics = song.lyrics
    preprocessed_lyrics = Util.remove_stopwords_and_punctuation(preprocessed_lyrics)
    preprocessed_lyrics = Util.remove_trash_words(preprocessed_lyrics)
    preprocessed_lyrics = Util.remove_symbols(preprocessed_lyrics)
    preprocessed_lyrics, word_mapping = Util.lemmatize(preprocessed_lyrics)
    word_mapping = Util.reverse_dict(word_mapping)

    for category, category_values in lemmatized_categories.items():
        check_against_category(preprocessed_lyrics, word_mapping, song, category, category_values)


def check_against_category(preprocessed_lyrics_temp: str, word_mapping: Dict[str, List[str]], song_temp: Song,
                           category: str, category_values: Tuple[str, str]):
    if song_temp.matched_categories is None:
        song_temp.matched_categories = {}
    counted_words = Counter(preprocessed_lyrics_temp.split())
    for word, count in counted_words.most_common():
        if word in list(map(lambda x: x[1], category_values)):
            if category in song_temp.matched_categories:
                song_temp.matched_categories[category].append((word, count, word_mapping[word]))
            else:
                song_temp.matched_categories[category] = [(word, count, word_mapping[word])]


def check_against_category_without_mapping(preprocessed_lyrics: str,
                                           song_temp: Song, category: str, category_values: List[str]):

    if song_temp.matched_categories is None:
        song_temp.matched_categories = {}
    counted_words = Counter(preprocessed_lyrics.split())
    matched_categories = {}
    for word, count in counted_words.most_common():
        for category_value in category_values:
            # also allow substrings to be matched
            # if one of the words in the lyrics starts with or ends with a word of the categories then consider them always
            # if a word of the lyrics of a substring is part of a word of the category value only consider them if
            # this word is at least 75% equal to the given category value
            bool1 = word in category_value and len(word) >= 0.75 * len(category_value)
            bool2 = word.startswith(category_value) or word.endswith(category_value)
            if bool1 or bool2:
                matched_categories[word] = count

    if matched_categories:
        song_temp.matched_categories[category] = matched_categories



def sum_occurences_over_time(songs_dict) -> pd.DataFrame:
    columns = [str(i) for i in range(1998, 2024)]
    index = list(categories.categories.keys()) + ['number_of_songs'] + \
            [key + "_normalized" for key, _ in categories.categories.items()]
    results = pd.DataFrame(0,
                           index=index,
                           columns=columns)
    for song in songs_dict.song_list:
        if song.release_date not in [None, "unidentified"]:
            year = song.release_date[0:4]
            if year in columns:
                results.at['number_of_songs', year] += 1
            for category, matched_word_dict in song.matched_categories.items():
                if year in columns:
                    results.at[category, year] = results.at[category, year] + \
                                                 sum([count for word, count in matched_word_dict.items()])

    for year in columns:
        for category, _ in categories.categories.items():
            if results.at['number_of_songs', year] != 0:
                results.at[category + "_normalized", year] = \
                    round(float(results.at[category, year]) / float(results.at['number_of_songs', year]), 2)
            else:
                results.at[category + "_normalized", year] = 0

    return results
