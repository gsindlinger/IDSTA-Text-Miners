import csv
from typing import Dict
from lyricsgenius import Genius

from Pipeline.Artist_Generation.ArtistCollection import ArtistCollection

"""
File is mainly used to do some preprocessing for scraping the wep page of Genius.com.
The described methods and classes are used to extract the ids of the artists given an ArtistCollection.
These ideas are later used to send url requests to scrape data from the web page via BeatifoulSoup.
"""


class GeniusArtists:
    def __init__(self, genius: Genius | None = None):
        self.id_list: Dict[str, int] = {}
        self.genius: Genius | None = genius

    def __len__(self):
        return len(self.id_list)

    def write_csv(self, filename: str) -> None:
        with open(filename, "w", newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            for key, value in self.id_list.items():
                writer.writerow([key, str(value)])

    def load_artist_ids(self, artist_collection: ArtistCollection):
        for artist in artist_collection.get_artist_name_list():
            result = self.get_artist_id_via_genius(artist)
            try:
                if list(result.keys())[0].lower() == artist.lower():
                    self.id_list.update(result)
                    print("Found a match!")
            except:
                print("No Found")

    def get_artist_id_via_genius(self, artist_name: str) -> Dict[str, int]:
        genius_artist = self.genius.search_artist(artist_name, max_songs=0, sort="title")
        try:
            if genius_artist.name == artist_name:
                results = {genius_artist.name: genius_artist.id}
                return results
        except:
            print('no result found')


def load_artist_ids(artist_collection: ArtistCollection, genius: Genius) -> GeniusArtists:
    genius_artists = GeniusArtists(genius)
    genius_artists.load_artist_ids(artist_collection)
    return genius_artists


"""
Reading the artists_id_list and dumping into a dictionary
"""


def csv_to_artist_id_dict(filename: str) -> GeniusArtists:
    genius_artists = GeniusArtists()
    with open(filename, encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        genius_artists.id_list = dict((x[0], int(x[1])) for x in reader)
    return genius_artists
