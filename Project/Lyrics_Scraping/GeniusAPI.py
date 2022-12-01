# adopted from https://medium.com/analytics-vidhya/how-to-scrape-song-lyrics-a-gentle-python-tutorial-5b1d4ab351d2

import requests
import config


class GeniusAPI:
    def __init__(self):
        self.__client_id: str = config.CLIENT_ID
        self.__client_secret: str = config.CLIENT_SECRET
        self.__access_token: str = config.ACCESS_TOKEN
        self.__base_url: str = 'https://api.genius.com'

    def request_artist_info(self, artist_name: str):
        headers = {'Authorization': 'Bearer ' + self.__access_token}
        search_url = self.__base_url + '/search'
        data = {'q': artist_name}

        response = requests.get(search_url, data=data, headers=headers)
        json = response.json()
        print(json)
