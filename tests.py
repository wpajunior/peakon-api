import unittest
from unittest.mock import call, patch
import peakon.client


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.test_token = 'test_token'
        self.client = peakon.client.Client(self.test_token)


@patch('requests.get')
class TestClient(BaseTestCase):
    def test_get(self, requests_get):
        test_path = 'engagement/drivers'

        requests_get.return_value.json.return_value = {}

        self.client.get(test_path)

        self.assertEqual(requests_get.called, True)

        (uri,), kwargs = requests_get.call_args
        self.assertEqual(uri, self.client.api_base_url + test_path)
        self.assertEqual(kwargs['stream'], False)
        self.assertEqual(kwargs['headers']['Authorization'], 'Bearer ' + self.test_token)
    
    def test_get_http_error(self, requests_get):
        test_path = 'engagement/drivers'

        requests_get.return_value.json.return_value = {'status': 500, 'message': 'Application Error' }
        self.client.get(test_path)

    
    def create_object_with_json_function(self):
        obj = object()
        obj.json = lambda: '{}'


@patch.object(peakon.client.Client, 'get')
class TestDrivers(BaseTestCase):
    def test_find_by_context_no_optional_parameters(self, client_get):
        test_segment = 'segment_123'

        self.client.drivers.find_by_context(test_segment)
        self.assertEqual(client_get.called, True)
        (path,), _ = client_get.call_args
        self.assertEqual(path, 'engagement/contexts/{}/drivers'.format(test_segment))
    
    def test_find_by_context_all_optional_parameters(self, client_get):
        test_segment = 'segment_123'
        filter = 'filter[question.driver]=autonomy'

        self.client.drivers.find_by_context(test_segment, filter, observations=True, participation=True, interval='all')
        self.assertEqual(client_get.called, True)
        (path,), _ = client_get.call_args
        self.assertEqual(path, 'engagement/contexts/{}/drivers?{}&observations=true&participation=true&interval=all'.format(test_segment, filter))


@patch.object(peakon.client.Client, 'get')
class TestSegments(BaseTestCase):
    def test_find_by_type_no_optional_parameters(self, client_get):
        test_type = 'employee'

        self.client.segments.find_by_type(test_type)
        self.assertEqual(client_get.called, True)
        (type,), _ = client_get.call_args
        self.assertEqual(type, 'segments?filter[type]={}'.format(test_type))

if __name__ == '__main__':
    unittest.main()