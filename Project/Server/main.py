from Pipeline.Lyrics_Scraping import GeniusLyricsExtraction
from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import GeniusSongs
from Pipeline.Lyrics_Scraping.Song import Song
from Server.ElasticsearchConnection import ElasticsearchConnection

if __name__ == '__main__':

    es = ElasticsearchConnection()
    test_str = Song.get_song_mapping()

    index_name = "test"
    # es.create_index(index_name, test_str)
    # Read json to GeniusSongs object
    songs: GeniusSongs = GeniusLyricsExtraction.read_song_list("Pipeline/Lyrics_Scraping/data/lyrics.json")
    # es.insert_one_data(index_name, songs.song_list[0])
    # es.insert_bulk(index_name, songs)
    test_song = es.get_by_id(index_name, songs.song_list[0].genius_track_id)
    test_song = es.get_by_artist_id(index_name, songs.song_list[0].artist_id)
    print("Hallo")
