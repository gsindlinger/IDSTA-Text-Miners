from Pipeline.Lyrics_Scraping import GeniusLyricsExtraction
from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import GeniusSongs
from Pipeline.Lyrics_Scraping import Song
from Server.ElasticsearchConnection import ElasticsearchConnection

if __name__ == '__main__':

    es = ElasticsearchConnection()
    test_str = Song.get_song_mapping()

    index_name = "lyrics_data"
    es.create_index(index_name, test_str)
    # Read json to GeniusSongs object
    songs: GeniusSongs = GeniusLyricsExtraction.read_song_list("../Pipeline/Analysis/data/lyrics_updated_v2.json")
    # es.insert_one_data(songs.song_list[0], index_name)
    es.insert_bulk(songs, index_name)
    # test_song = es.get_by_id(index_name, songs.song_list[0].genius_track_id)
    # test_song = es.get_by_artist_id(index_name, songs.song_list[0].artist_id)
    print("Done")
