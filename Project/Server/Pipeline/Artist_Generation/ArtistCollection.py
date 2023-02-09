import csv
from typing import Set, Dict, List

from Pipeline.Artist_Generation import config
from Pipeline.Artist_Generation.SpotifyConnection import SpotifyConnection


class ArtistCollection:
    def __init__(self):
        self.list: Dict[str, Set[int]] = {}

    def append_item(self, name: str, year: int) -> None:
        if self.is_existing_artist(name):
            self.get_year_set(name).add(year)
        else:
            self.list.update({name: {year}})

    def is_existing_artist(self, name: str) -> bool:
        if name in self.list:
            return True
        else:
            return False

    def get_year_set(self, name: str) -> Set[int]:
        try:
            return self.list[name]
        except KeyError:
            print("Artist name doesn't exist!")

    def write_to_csv(self, filename: str) -> None:
        with open(filename, "w", newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            for name, years in self.list.items():
                row = [name]
                row.extend(list(map(str, years)))
                writer.writerow(row)

    def get_artist_name_list(self) -> List[str]:
        return list(self.list.keys())


def read_csv_to_artist_collection(filename: str) -> ArtistCollection:
    artist_collection = ArtistCollection()
    with open(filename, encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            name = row.pop(0)
            years = set([int(y) for y in row])
            artist_collection.list.update({name: years})

    return artist_collection


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

    artist_collection.write_to_csv('data/artist_data.csv')
