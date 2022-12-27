from ArtistCollection import ArtistCollection, read_csv_to_artist_collection, collect_artist_data


if __name__ == '__main__':
    """
    Choose which method to use. Read the data from API, which requires credentials or read a csv file to
    ArtistCollection object.
    """
    # collect_artist_data()
    artist_collection: ArtistCollection = read_csv_to_artist_collection("data/artist_data.csv")
