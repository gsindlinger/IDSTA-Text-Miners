from Artist_Generation.ArtistCollection import ArtistCollection, read_csv_to_artist_collection
from Lyrics_Scraping.GeniusAPI import GeniusAPI

if __name__ == '__main__':
    artist_collection = read_csv_to_artist_collection("../Artist_Generation/data/artist_data_single.csv")

    genius_api = GeniusAPI()
    print(artist_collection.list.keys())
    genius_api.request_artist_info(list(artist_collection.list.keys())[0])
    print("Reading artist collection done!")
