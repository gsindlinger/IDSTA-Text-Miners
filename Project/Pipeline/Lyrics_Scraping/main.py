from lyricsgenius import Genius

from Pipeline.Artist_Generation.ArtistCollection import read_csv_to_artist_collection
from Pipeline.Lyrics_Scraping import GeniusArtistExtraction
from Pipeline.Lyrics_Scraping.GeniusArtistExtraction import GeniusArtists
from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import get_songs, GeniusSongs, read_song_list
from Pipeline.Lyrics_Scraping.config import CLIENT_ACCESS_TOKEN

if __name__ == '__main__':

    genius = Genius(CLIENT_ACCESS_TOKEN)

    '''
    # Load artists
    artist_collection = read_csv_to_artist_collection("../Artist_Generation/data/artist_data.csv")

    # Get Genius ids for artists
    genius_artists: GeniusArtists = GeniusArtistExtraction.load_artist_ids(artist_collection, genius)
    print('Loading Artist ids done')
    
    # Write artists to csv
    genius_artists.write_csv("data/artist_id_list.csv")
    '''

    # Read genius artists id / name to object
    genius_artists: GeniusArtists = GeniusArtistExtraction\
        .csv_to_artist_id_dict("data/artist_id_list.csv")

    # Scrape songs via artist id
    songs: GeniusSongs = get_songs(genius_artists)

    # Write songs to json
    songs.write_song_list_to_json("data/refactored/lyrics.json")

    # Read json to GeniusSongs object
    songs: GeniusSongs = read_song_list("data/lyrics.json")
