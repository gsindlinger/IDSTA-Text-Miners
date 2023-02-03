from typing import List

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from Pipeline.Lyrics_Scraping.GeniusLyricsExtraction import GeniusSongs
from Pipeline.Lyrics_Scraping.Song import Song
from Server.ElasticsearchConnection import ElasticsearchConnection



class SearchQuery(BaseModel):
    text: str


app = FastAPI()
es = ElasticsearchConnection()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {'success': True, 'message': 'healthy :)'}


# endpoint that allows users to search on the frontend
@app.post("/search")
def search(search_query: SearchQuery):
    res: List[Song] | None = es.search_in_title_and_lyrics(search_query.text)
    if res is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        res_songs = GeniusSongs()
        res_songs.song_list = res
        return {"query": search_query.text, 'success': True, 'results': res_songs.write_song_list_to_str()}

# get random song
@app.get("/random")
def get_random_song():
    res: Song | None = es.get_random_song()
    if res is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return {'success': True, 'results': res.write}


@app.get("/")
def root():
    return {"Hello": "World :)"}
