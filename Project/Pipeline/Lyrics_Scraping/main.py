from lyricsgenius import Genius

from Pipeline.Artist_Generation.ArtistCollection import read_csv_to_artist_collection
from Pipeline.Lyrics_Scraping import GeniusArtistExtraction
from Pipeline.Lyrics_Scraping.GeniusArtistExtraction import GeniusArtists
from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import get_songs, GeniusSongs, read_song_list, GeniusSongsDict, \
    read_song_dict
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

    '''
    # Read genius artists id / name to object
    genius_artists: GeniusArtists = GeniusArtistExtraction\
        .csv_to_artist_id_dict("data/artist_id_list.csv")

    # Scrape songs via artist id
    songs: GeniusSongs = get_songs(genius_artists)

    # Write songs to json
    songs.write_song_list_to_json("data/refactored/lyrics.json")
    '''

    # Read json to GeniusSongs object
    songs: GeniusSongs = read_song_list("data/lyrics.json")
    # Convert to Dict Object for better readability with artist name as key
    songs_dict: GeniusSongsDict = songs.to_song_dict()
    # Write with artist name as key to json
    songs_dict.write_song_dict_to_json("data/lyrics_dict_structure.json")
    # Load dict with artist name as key to json
    songs_dict_loaded: GeniusSongsDict = read_song_dict("data/lyrics_dict_structure.json")
