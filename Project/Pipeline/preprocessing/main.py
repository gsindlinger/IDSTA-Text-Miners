from Pipeline.Lyrics_Scraping import GeniusLyricsExtraction
from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import GeniusSongsDict, GeniusSongs
from Pipeline.preprocessing import CheckOccurences
from Pipeline.preprocessing.CategoryDictionary import CategoryDictionary, read_from_json

if __name__ == '__main__':
    '''
    w2v_dictionary = CategoryDictionary()
    print('model loaded')
    w2v_dictionary.build_dictionary_model()
    print('dictionary computed')

    '''
    songs_dict: GeniusSongs = GeniusLyricsExtraction.read_song_list_from_json_dict("data/punctuated_german_lyrics.json")
    songs_dict.song_list = songs_dict.song_list[:5]

    w2v_dictionary_loaded: CategoryDictionary = read_from_json("data/categories.json")
    CheckOccurences.check_occurences_songs(songs_dict)
    # CheckOccurences.sum_occurences_over_time(songs_dict)
    
    '''
    
    songs_dict.write_song_list_to_json("data/checked_occurences_lyrics.json")
    '''
    print("done")
