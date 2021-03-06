class Source:
  '''
  Source class to define Source objects
  '''

  def __init__(self, id, name, description, url, category, language, country):
    self.id = id
    self.name = name
    self.description = description
    self.url = url
    self.category = category
    self.language = language
    self.country = country


class Article:
  '''
  Articles class to define Article objects
  '''

  def __init__(self, author, title, imageurl, publishedAt, url):
    self.author = author
    self.title = title
    self.imageurl =imageurl
    self.publishedAt = publishedAt
    self.url = url
