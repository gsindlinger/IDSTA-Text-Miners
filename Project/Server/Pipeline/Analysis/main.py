from Pipeline.Analysis.CategoryDictionary import CategoryDictionary
from Pipeline.Lyrics_Scraping import GeniusLyricsExtraction
from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import GeniusSongs
from Pipeline.Analysis import CheckOccurences, PretrainedModels

if __name__ == '__main__':
    """
    # build the dictionary of categories
    w2v_dictionary = CategoryDictionary()
    print('model loaded')
    w2v_dictionary.build_dictionary_model()
    print('dictionary computed')
    """

    # read songs from json file
    songs_list: GeniusSongs = GeniusLyricsExtraction \
        .read_song_list("data/lyrics_updated_v2.json")
    # check occurrences of words withing the categories
    # CheckOccurences.check_occurences_songs(songs_list)

    # get values for the pretrained models
    # PretrainedModels.calc_sentiment_bert(songs_list)
    # PretrainedModels.calc_toxicity(songs_list)

    # write the updated songs to file
    # songs_list.write_song_list_to_json("data/lyrics_updated.json")

    # analyze the results
    # occurrences_df = CheckOccurences.sum_occurences_over_time(songs_list)
    # occurrences_df.to_csv("data/analysis/occurrences_over_time.csv")

    print("done")
