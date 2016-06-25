import os.path
import unittest
from urlparse import urlparse

from client import ClientAPI
from mock import patch

def fake_urlopen(url):

    parsed_url = urlparse(url)
    resource_file = os.path.normpath("tests/resources%s" % parsed_url.path)
    return open(resource_file, mode='rb')


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.patcher = patch('client.urlopen', fake_urlopen)
        self.patcher.start()
        self.client = ClientAPI()

    def tearDown(self):
        self.patcher.stop()

    def test_request(self):
        user = 'test_user'
        response = self.client.request(user)
        self.assertIn('name',response)
        self.assertEqual(response['name'], 'Test User')
