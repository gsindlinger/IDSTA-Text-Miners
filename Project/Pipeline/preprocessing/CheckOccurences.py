from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import GeniusSongs
from Pipeline.Lyrics_Scraping.Song import Song
from Pipeline.preprocessing.CategoryDictionary import CategoryDictionary
import Util


def check_occurences(categories: CategoryDictionary, songs: GeniusSongs) -> None:
    for song in songs.song_list:
        check_occurences(categories, song)


def check_occurences(categories: CategoryDictionary, song: Song) -> None:
    preprocessed_lyrics = song.lyrics
    preprocessed_lyrics = Util.remove_stopwords_and_punctuation(preprocessed_lyrics)
    preprocessed_lyrics = Util.remove_trash_words(preprocessed_lyrics)
    preprocessed_lyrics = Util.lemmatize(preprocessed_lyrics)

    for category, category_values in categories.categories:
        check_against_category(preprocessed_lyrics, song, category, category_values)

def check_against_category(preprocessed_lyrics, song, category, category_values):
    for word in preprocessed_lyrics.split():
        if word in list(map(lambda x: x[1], category_values)):
            if song.matched_categories[category]:
                song.matched_categories.update({category: []})
            temp_list = song.matched_categories[category]