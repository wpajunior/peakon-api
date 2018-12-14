import requests
from peakon.resources.drivers import Drivers
from peakon.resources.segments import Segments


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
        self.drivers = Drivers(self)
        self.segments = Segments(self)
    
    def get(self, path):
        """ Makes the get request to the API """
        result = requests.get(self.api_base_url + path, headers=self.__http_header, stream=False, timeout=60).json()

        try:
            status = result['status']
            message = result['message']
        except KeyError:
            return result
        else:
            raise RuntimeError('Error fetching data status code: {}. Message: {}'.format(status, message))

    def __create_http_header(self):
        return {'Authorization': 'Bearer ' + self.token,
            'User-Agent': 'python',
            'Accept': 'application/json',
            'Content-Type': 'application/json'}

