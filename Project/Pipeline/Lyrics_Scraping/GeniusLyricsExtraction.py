import concurrent
import json
from typing import List

import requests
from bs4 import BeautifulSoup

from Pipeline.Lyrics_Scraping.GeniusArtistExtraction import GeniusArtists
from Pipeline.Lyrics_Scraping.Song import Song
from Pipeline.Lyrics_Scraping.config import CLIENT_ACCESS_TOKEN
from Pipeline.Util.Util import get_html_resource_to_json

SONGS_PER_ARTIST = 15
BASE = "https://api.genius.com"


class GeniusSongs:
    def __init__(self):
        self.song_list: List[Song] = []

    def __len__(self):
        return len(self.song_list)

    def write_song_list_to_json(self, filename: str) -> None:
        json_string = json.dumps([song.__dict__ for song in self.song_list])
        with open(filename, 'w', encoding='utf8') as f:
            f.write(json_string)


def read_song_list(filename: str) -> GeniusSongs:
    songs = GeniusSongs()
    with open(filename, 'r') as f:
        json_data = f.read()

    songs.song_list = json.loads(json_data)
    return songs


def get_songs_information(song_ids: List[str], artist_id: str, artist_name: str) -> GeniusSongs | None:
    song_list = GeniusSongs()

    print("Scraping songs information of artist {}".format(artist_name))
    for song_id in song_ids:
        path = "songs/{}".format(song_id)
        try:
            data = get_html_resource_to_json(BASE, path, CLIENT_ACCESS_TOKEN)['response']['song']
        except:
            print("failed to fetch information for song id {}".format(song_id))
            return

        song_temp = Song(genius_track_id=song_id)
        song_temp.artist_name = artist_name
        song_temp.artist_id = artist_id
        song_temp.title = data["title"] if data else ""
        song_temp.album = data["album"]["name"] if data["album"] else "<single>"
        song_temp.album_cover = data["album"]["cover_art_url"] if data["album"] and data["album"][
            "cover_art_url"] else ""
        song_temp.genius_album_id = data["album"]["id"] if data["album"] else "none"
        song_temp.release_date = data["release_date"] if data["release_date"] else "unidentified"
        song_temp.featured_artists = [feat["name"] if data["featured_artists"]
                                      else "" for feat in data["featured_artists"]]
        song_temp.featured_artist_pics = [feat["image_url"] if data["featured_artists"]
                                          else "" for feat in data["featured_artists"]]
        song_temp.producer_artists = [feat["name"] if data["producer_artists"]
                                      else "" for feat in data["producer_artists"]]
        song_temp.writer_artists = [feat["name"] if data["writer_artists"]
                                    else "" for feat in data["writer_artists"]]
        song_temp.primary_artist_picture = data["primary_artist"]["image_url"] \
            if data["primary_artist"]["image_url"] else ""
        song_temp.lyrics_path = data['path'] if data['path'] else 'none'
        song_temp.lyrics_status = data['lyrics_state']

        song_temp.lyrics = get_lyrics_from_path(song_temp.lyrics_path)

        # there are a few songs without any lyrics which will be ignored
        if len(song_temp.lyrics) > 5:
            song_list.song_list.append(song_temp)

    print("Scraped information for {} songs of artist {}".format(len(song_list), artist_name))
    return song_list


def get_song_id_list_of_artist(artist_id: str, page_limit: int,
                               songs_limit: int) -> List[str]:
    current_page = 1
    next_page = True
    songs = []

    while next_page and current_page <= page_limit:

        path = 'artists/{}/songs?page={}&sort=popularity'.format(artist_id, current_page)
        page = get_html_resource_to_json(BASE, path, CLIENT_ACCESS_TOKEN)['response']['songs']
        if page:
            for song in page:
                if song['primary_artist']['id'] == artist_id and song['lyrics_state'] == 'complete' and len(
                        songs) <= songs_limit:
                    songs.append(song['id'])
        else:
            next_page = False
        current_page += 1
    return list(dict.fromkeys(songs))  # remove duplicates if exist


def get_lyrics_from_path(lyrics_path: Song) -> str:
    if lyrics_path == 'none':
        return "none"
    URL = "http://genius.com" + lyrics_path
    page = requests.get(URL)

    # Extract the page's HTML as a string
    html = BeautifulSoup(page.text, "html.parser")

    # Scrape the song lyrics from the HTML
    output = ""
    for lyrics in html.select('div[class^="Lyrics__Container"]'):
        output += lyrics.get_text(strip=True, separator='\n')
    return output


# This function was originally written to batch scrap all artists
# Since we want concurrent multithreading, we must have changed it,
# so it only processes one artist
def batch_get_songs(artist_id: List[int], artist_name: List[str], songs_per_artist=SONGS_PER_ARTIST,
                    pages_to_scrape=5) -> GeniusSongs:
    song_ids: List[str] = get_song_id_list_of_artist(artist_id, pages_to_scrape, songs_per_artist)
    print("Fetched {} songs for {}, {}".format(len(song_ids), artist_name, artist_id))

    songs_information: GeniusSongs = get_songs_information(song_ids, artist_id, artist_name)
    return songs_information


def get_songs(artists: GeniusArtists) -> GeniusSongs:
    final_songs = GeniusSongs()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for result in executor.map(batch_get_songs,
                                   list(artists.id_list.values()),
                                   list(artists.id_list.keys())):
            final_songs.song_list.extend(result.song_list)

    return final_songs
