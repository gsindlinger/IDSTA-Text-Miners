from Pipeline.Lyrics_Scraping import GeniusLyricsExtraction
from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import GeniusSongsDict, GeniusSongs
from Pipeline.preprocessing.CategoryDictionary import CategoryDictionary, read_from_json

if __name__ == '__main__':
    '''
    w2v_dictionary = CategoryDictionary()
    print('model loaded')
    w2v_dictionary.build_dictionary_model()
    print('dictionary computed')

    songs_dict: GeniusSongs = GeniusLyricsExtraction.read_song_list_from_json_dict("only_german_lyrics.json")
    songs_dict = songs_dict.song_list[:10]

    '''
    w2v_dictionary_loaded = read_from_json("data/categories.json")
    print("done")
