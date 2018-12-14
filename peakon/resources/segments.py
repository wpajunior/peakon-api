class Segments:
    def __init__(self, client):
        self.client = client
    
    def find_by_type(self, type, per_page=None):
        """
        Fetches segments by type

        :param type: Type of the parameter: employee, option, date, number
        :type type: str
        :param per_page: Number of items per page to return
        :type per_page: int
        :returns: A dictionary containing a list of segiments with the specified type
        :rtype: dict
        :raises: RuntimeError
        """
        filter = 'filter[type]={}'.format(type)

        path = 'segments?' + filter

        if per_page:
            path += '&per_page=' + str(per_page)

        return self.client.get(path)
