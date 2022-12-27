# Lyrics scraping

The lyrics of the different artists specified via Spotify API and "Deutschrap xxx" playlists are scraped via Genius 
API and HTTP requests against the Genius webpage. 
As a basis for the code served the explanations of 
[Nick Pai / Medium.com](https://medium.com/analytics-vidhya/how-to-scrape-song-lyrics-a-gentle-python-tutorial-5b1d4ab351d2).

## The procedure

As a first step, for each artist of the artist list specified by the [Artist_Generation](../Artist_Generation) part, the
id of the speficied artist is loaded via search query against Genius API. The list of the artists to search for is given
by [artist_data.csv](../Artist_Generation/data/artist_data.csv) file in the Artist_Generation folder. The resulting
mapping of names of artists and ids of the Genius API is stored in [data/artist_id_list.csv](data/artist_id_list.csv) file.
The implementation of this procedures can be found in [GeniusArtistExtraction.py](GeniusArtistExtraction.py) file.

Then, this information is used to send another query against Genius API to get the most popular songs of each artist.
At the moment we limit the amount of songs to 15. For each song we extract the exact url of the Genius webpage, save
them for the next step. Furthermore, we extract all information given in the Genius API for each song. Due to limitations of
the Genius API, it is not possible to extract the lyrics data directly from the Genius API. In order to face this problem 
we scrape the lyrics of each of the songs by sending an HTTP request using the BeautifulSoup framework and enrich the 
already obtained data about the songs. Since all these steps take a considerable amount of computation time, these steps
are performed in a multithreaded manner. All the respective code can be found in 
[GeniusLyricsExtraction.py](GeniusLyricsExtraction.py) file. 

The resulting list of songs can be stored to local JSON  file or will be put into data pots like Elasticsearch. 
A glimpse of the way the resulting data looks like can be obtained via [lyrics.json](data/lyrics.json) file. 
This file contains the scraped songs for three of the selected artists.

## Getting started
1. if not already done, create Genius API credentials online. For the scraping process you need a client access token.
2. create a file called ``config.py`` in the Lyrics_Scraping folder and add the credentials with the names ``CLIENT_ACCESS_TOKEN``.
3. install requirements: ``` pip install -r requirements.txt```
4. modify the code in file ``main.py`` according to the functionality you want. For details check the comments of the file.
5. run ```python .\main.py```

