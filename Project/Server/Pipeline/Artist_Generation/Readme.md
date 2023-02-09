# Artist generation

The artists for scraping via Genius were determined using the Spotify API. The playlists "Deutschrap xxxx" were used, where "xxxx" stands for a year in the period 1998-2022. For each year, either only the official Spotify playlist is selected or multiple playlists from different creators.

For the first alternative, the file [data/artist_data_single.csv](data/artist_data.csv) was created as an example, for the second alternative the file [data/artist_data.csv](data/artist_data.csv). The generated CSV files can be read via read_csv_to_artist_collection method in the [ArtistCollection.py](ArtistCollection.py) file / module.

## The procedure
For each playlist requested with the search query "Deutschrap xxxx", all artists are extracted and then added to the ArtistCollection. Thereby it is checked if the artist already exists: If yes, only one entry is added for this artist for the concerned year, so that each artist appears only once in the ArtistCollection.


## Getting started
1. if not already done, create Spotify API credentials online.
2. create a file called ``config.py`` and add the credentials with the names ``SPOTIFY_CLIENT_ID`` and
``SPOTIFY_CLIENT_SECRET``.
3. install requirements: ``` pip install -r requirements.txt```
4. modify the code in file ``main.py`` according to the functionality you want.
5. run ```python .\main.py```

