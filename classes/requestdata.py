import requests
from typing import Dict


class RequestToMaze:
    
    def __init__(self):
        self.querystring = {'q': 'SouthPark'} # params for url struct
        self.api = 'https://api.tvmaze.com/search/shows' # default link
    
    def send_request(self) -> Dict:
        self.source = requests.get(self.api, params=self.querystring)
        return self.source.json()[0]['show'] # Returns the first dict of a list with show key only to parse into database
    
    def update_query_string(self, new_query_string: str) -> None:
        self.querystring = new_query_string
