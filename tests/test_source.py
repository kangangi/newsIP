import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set-up method that runs before any test
        '''
        self.new_source = Source(
            "abc-news", "ABC News", "Your trusted source", "siteUrl", "general", "en", "us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))
