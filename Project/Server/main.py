from Pipeline.Lyrics_Scraping import Song, GeniusLyricsExtraction
from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import GeniusSongs
from Server.ElasticsearchConnection import ElasticsearchConnection
import configparser

if __name__ == '__main__':

    es = ElasticsearchConnection()
    test_str = Song.get_song_mapping()
    es.create_index("test", test_str)
    # Read json to GeniusSongs object
    songs: GeniusSongs = GeniusLyricsExtraction.read_song_list("data/lyrics.json")
    print("Hallo")
