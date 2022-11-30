from Artist_Generation.ArtistCollection import ArtistCollection


if __name__ == '__main__':
    artist_collection = ArtistCollection()
    artist_collection.read_csv_to_object("../Artist_Generation/data/artist_data_single.csv")
    print("Reading csv done!")
