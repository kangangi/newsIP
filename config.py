class Config:
  '''
  General configuration parent class
  '''
  NEWS_API_TOP_ARTICLES_BASE_URL = 'http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
  NEWS_API_SOURCES_BASE_URL = 'http://newsapi.org/v2/sources?&apiKey={}'
  NEWS_API_KEY = '6d0385bc4d6d4426a13dd274096ee2d8'


class ProdConfig(Config):
  '''
  Production  configuration child class

  Args:
    Config: The parent configuration class with General configuration settings
  '''
  pass


class DevConfig(Config):
  '''
  Development  configuration child class

  Args:
    Config: The parent configuration class with General configuration settings
  '''

  DEBUG = True
