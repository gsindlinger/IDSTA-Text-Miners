from Pipeline.Lyrics_Scraping import GeniusLyricsExtraction
from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import GeniusSongsDict, GeniusSongs
from Pipeline.preprocessing import CheckOccurences, PretrainedModels
from Pipeline.preprocessing.CategoryDictionary import CategoryDictionary, read_from_json

if __name__ == '__main__':
    '''
     # build the dictionary of categories
    w2v_dictionary = CategoryDictionary()
    print('model loaded')
    w2v_dictionary.build_dictionary_model()
    print('dictionary computed')
    '''

    # read songs from json file
    songs_list: GeniusSongs = GeniusLyricsExtraction.read_song_list_from_json_dict("data/punctuated_german_lyrics.json")

    # check occurrences of words withing the categories
    w2v_dictionary_loaded: CategoryDictionary = read_from_json("data/categories.json")
    CheckOccurences.check_occurences_songs(songs_list)

    # get values for the pretrained models
    PretrainedModels.calc_sentiment_bert(songs_list)
    PretrainedModels.calc_toxicity(songs_list)

    # write the updated songs to file
    songs_dict: GeniusSongsDict = songs_list.to_song_dict()
    songs_dict.write_song_dict_to_json("data/punctuated_german_lyrics_updated.json")

    # analyze the results
    occurrences_df = CheckOccurences.sum_occurences_over_time(songs_list)
    occurrences_df.to_csv("data/analysis/occurrences_over_time.csv")
    '''
    
    songs_dict.write_song_list_to_json("data/analysis/checked_occurrences_lyrics.json")
    '''
    print("done")
