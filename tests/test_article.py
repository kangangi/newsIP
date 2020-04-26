import unittest
from models import Article


class ArticleTest(unittest.TestCase):
  '''
  Test class to test the behaviour of the Article class
  '''

  def setUp(self):
    '''
    Set-up method that runs before any test
    '''
    self.new_article = Article("Corona virus","James Doe", "Date", "siteUrl")

  def test_instance(self):
    self.assertTrue(isinstance(self.new_article,Article))
