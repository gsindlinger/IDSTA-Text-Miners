import config
from ArtistCollection import ArtistCollection
from SpotifyConnection import SpotifyConnection


def collect_artist_data() -> None:
    sp_connection = SpotifyConnection(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET)
    sp_object = sp_connection.connect()
    artist_collection = ArtistCollection()

    for i in range(1998, 2023):
        print("Start querying playlists for", i)
        playlist_results = sp_object.search(q="Deutschrap " + str(i), type="playlist")
        playlist_results_items = playlist_results['playlists']['items']

        """
        If only the playlists created by the official Spotify account should be selected, then use the if query below.
        If one wants to select multiple playlists from different creators, one can use the out commented code with the 
        for-loop.
        """
        # for j in range(min(4, len(playlist_results_items))):
        if playlist_results_items[0]['owner']['id'] == 'spotify':
            query_playlist = playlist_results_items[0]
            # query_playlist = playlist_results_items[j]
            playlist = sp_object.playlist(query_playlist['id'])
            tracks = list(map(lambda tr: tr['track']['artists'], playlist['tracks']['items']))

            for track in tracks:
                for artist in track:
                    artist_collection.append_item(artist['name'], i)

    artist_collection.write_to_csv('data/artist_data_single.csv')


def read_artist_data() -> None:
    artist_collection = ArtistCollection().read_csv_to_object("data/artist_data_single.csv")
    print("Reading csv done!")


if __name__ == '__main__':
    """
    Choose which method to use. Read the data from API, which requires credentials or read a csv file to
    ArtistCollection object.
    """
    read_artist_data()
    #collect_artist_data()

