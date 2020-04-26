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


def process_results(source_list):
  '''
  Function that processes the source result and transforms them to a list of objects

  Args:
   source_list: A list of dictionaries that contain source details
  Returns:
    source_results: A list of source objects
  '''
  sources_available = []
  for source_item in source_list:
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    url = source_item.get('url')
    category = source_item.get('category')
    language = source_item.get('language')
    country = source_item.get('country')

    source_object = Source(id, name, description, url,category, language, country)
    sources_available.append(source_object)

  return sources_available


def get_sources():
  '''
  Function that gets the json response to our url request
  '''
  get_sources_url = base_url.format(api_key)
  print("-"*50)
  print(get_sources_url)
  print("-"*50)

  with urllib.request.urlopen(get_sources_url) as url:
    get_sources_data = url.read()
    get_sources_response = json.loads(get_sources_data)

  source_results = None

  if get_sources_response['sources']:
    source_results_list = get_sources_response['sources']
    source_results = process_results(source_results_list)

  return source_results


def get_top_articles(id):
  '''
  Function that gets the json response to our url request
  '''
  get_articles_details_url = top_articles_url.format(id, api_key)
  print("-"*50)
  print(get_articles_details_url)
  print("-"*50)

  article_details_data = url.read()
  article_details_response = json.loads(article_details_data)

   if article_details_response['articles']:
      article_list = article_details_response['articles']

    articles_available = []
    for article in article_list:
      author = article.get('author')
      title = article.get('title')
      publishedAt = article.get('publishedAt')
      url = article.get('url')


      article_object = Article(author, title, publishedAt, url)

      articles_available.append(article_object)

  return articles_available
