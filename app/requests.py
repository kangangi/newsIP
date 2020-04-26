import urllib.request.json
from models import Source,Article

#Getting Api key 
api_key = None

#Getting base urls
base_url = None
top_articles_url = None

def configure_request(app):
  global api_key, base_url, top_articles_url
  api_key = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_SOURCES_BASE_URL']
  top_articles_url = app.config['NEWS_API_TOP_ARTICLES_BASE_URL']
