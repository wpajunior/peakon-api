class Drivers:
    def __init__(self, client):
        self.client = client
    

    def find_by_context(self, context, filter=None, observations=False, participation=False, interval=None):
        """
        Fetches driver data from the specified context id

        :param context: Context id to fetch the data
        :type context: str
        :param filter: Data filter. Ex.: filter[question.driver]=autonomy
        :type filter: str
        :param observations: Indicates whether the observations data should be included or not
        :type observations: bool
        :param observations: Indicates whether the participation data should be included or not
        :type observations: bool
        :param interval: Data interval: month, quarter, year, all, recent
        :type interval: str
        :returns: A dictionary containing a list of drivers data for the specified context id
        :rtype: dict
        :raises: RuntimeError
        """
        parameters = []

        if filter:
            parameters.append(filter)
        
        if observations:
            parameters.append('observations=true')
        
        if participation:
            parameters.append('participation=true')
        
        if interval:
            parameters.append('interval=' + interval)

        path = 'engagement/contexts/{}/drivers'.format(context) + ('?' if len(parameters) > 0 else '') + '&'.join(parameters)

        return self.client.get(path)