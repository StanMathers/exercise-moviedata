import requests
from typing import Dict

class RequestToMaze:
    
    def __init__(self):
        self.querystring = {'q': 'SouthPark'} # params for url struct
        self.api = 'https://api.tvmaze.com/search/shows' # default link
    
    def send_request(self) -> Dict:
        try:
            self.source = requests.get(self.api, params=self.querystring)
            return self.source.json()[0]['show'] # Returns the first dict of a list with show key only to parse into database
        except IndexError:
            return False
    
    def first_movie_id(self):
        if self.send_request() != False:
            return self.send_request()['id']
    
    def update_query_string(self, new_query_string: str) -> None:
        self.querystring['q'] = new_query_string

if __name__ == '__main__':
    req = RequestToMaze()
    req.update_query_string('pp')
    
    print(req.send_request())

