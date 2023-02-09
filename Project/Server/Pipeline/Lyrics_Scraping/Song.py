from datetime import datetime
from typing import List, Dict, Tuple


class Song:
    def __init__(self, genius_track_id=None, genius_album_id=None, artist_name=None,
                 artist_id=None, title=None, album=None,
                 album_cover=None, release_date=None, featured_artists=None,
                 featured_artists_pics=None, producer_artists=None, writer_artists=None,
                 primary_artist_picture=None, lyrics_path=None, lyrics_status=None,
                 lyrics=None, matched_categories=None, processed_lyrics_text=None,
                 sentiment_value=None, toxicity_value=None, class_score_list=None, total_class_score=None):
        self.genius_track_id: str | None = genius_track_id
        self.genius_album_id: str | None = genius_album_id
        self.artist_name: str | None = artist_name
        self.artist_id: str | None = artist_id
        self.title: str | None = title
        self.album: str | None = album
        self.album_cover: str | None = album_cover
        self.release_date: str | None = release_date
        self.featured_artists: List[str] | None = featured_artists
        self.featured_artist_pics: List[str] | None = featured_artists_pics
        self.producer_artists: List[str] | None = producer_artists
        self.writer_artists: List[str] | None = writer_artists
        self.primary_artist_picture: str | None = primary_artist_picture
        self.lyrics_path: str | None = lyrics_path
        self.lyrics_status: str | None = lyrics_status
        self.lyrics: str | None = lyrics
        self.processed_lyrics_text: List[str] | None = processed_lyrics_text
        self.matched_categories: Dict[str, Dict[str, int] | int] | None = matched_categories
        self.sentiment_value: float | None = sentiment_value
        self.toxicity_value: float | None = toxicity_value
        self.class_score_list: List[Dict] | None = class_score_list
        self.total_class_score: Dict[str, float] | None = total_class_score

    def __str__(self):
        return f"Title: {self.title}, Artist: {self.producer_artists}, Id: {self.genius_track_id}"

    def flatten_matching_categories(self) -> None:
        if self.matched_categories is not None:
            matched_categories_new = {}
            for key, value_list in self.matched_categories.items():
                matched_categories_new[key] = sum(value_list.values())
            self.matched_categories = matched_categories_new

def get_song_mapping() -> Dict:
    type_keyword = {"type": "keyword"}
    type_text = {"type": "text"}
    type_date = {"type": "date"}
    type_mixed = {"type": "text",
                  "fields": {"raw": {"type": "keyword"}}}

    song_helper = Song()
    property_mapping = {}
    for variable, _ in song_helper.__dict__.items():
        match variable:
            case "genius_track_id":
                property_mapping.update({variable: type_keyword})
            case "genius_album_id":
                property_mapping.update({variable: type_keyword})
            case "artist_name":
                property_mapping.update({variable: type_mixed})
            case "artist_id":
                property_mapping.update({variable: type_keyword})
            case "title":
                property_mapping.update({variable: type_mixed})
            case "album":
                property_mapping.update({variable: type_mixed})
            case "album_cover":
                property_mapping.update({variable: type_keyword})
            case "release_date":
                property_mapping.update({variable: type_date})
            case "featured_artists":
                property_mapping.update({variable: type_keyword})
            case "featured_artist_pics":
                property_mapping.update({variable: type_keyword})
            case "producer_artists":
                property_mapping.update({variable: type_keyword})
            case "writer_artists":
                property_mapping.update({variable: type_keyword})
            case "primary_artist_picture":
                property_mapping.update({variable: type_keyword})
            case "lyrics_path":
                property_mapping.update({variable: type_keyword})
            case "lyrics_status":
                property_mapping.update({variable: type_keyword})
            case "lyrics":
                property_mapping.update({variable: type_text})
            case _:
                print(f"Mapping could not be found for: {variable}")

    return {
        "properties": property_mapping
    }



def dict_to_song(dict_temp: Dict) -> Song:
    song = Song()
    for key in dict_temp:
        song.__setattr__(key, dict_temp[key])
    return song
