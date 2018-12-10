import requests
import pdb


class Client(object):
    """ Peakon client class """
    def __init__(self, token):
        """ Creates a api client instance from a access token

        :param token: Acccess token
        :type token: str
        """
        self.token = token
        self.api_base_url = 'https://api.peakon.com/v1/'
        self.__http_header = self.__create_http_header()
    
    def get(self, path, filter):
        """ Makes the get request to the API """
        response = requests.get(self.api_base_url + path, headers=self.__http_headers, stream=False).json()
    

    def __create_http_header(self):
        return {'Authorization': 'Bearer ' + self.token,
            'User-Agent': 'python',
            'Accept': 'application/json',
            'Content-Type': 'application/json'}

