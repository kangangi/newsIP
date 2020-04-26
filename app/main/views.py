from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources,get_top_articles
from ..models import Source,Article

#Views
@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  sources = get_sources()
  title = "News-App"

  return render_template('index.html', title=title, sources=sources)
