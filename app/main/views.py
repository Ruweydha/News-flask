from unicodedata import name
from flask import render_template
from . import main
from ..requests import get_source, view_source
from ..models import Source, News

#views
@main.route('/')
def index():
    '''
    View root page function that returns the home page and it's data
    '''
    #Getting general news
    general_sources = get_source('business')
    news = view_source('abc-news')

    print(general_sources)
    title = 'Home - Welcome to News Api'

    return render_template('index.html', title = title, general = general_sources, articles = news)

@main.route('/source/<id>')
def source(id):
    sources = view_source(id)

    print(sources)
    # name = f'{sources.name}'

    return render_template('source.html', article = sources )
