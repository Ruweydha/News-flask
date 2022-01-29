from flask import render_template
from . import main
from ..requests import get_source
from ..models import Source

#views
@main.route('/')
def index():
    '''
    View root page function that returns the home page and it's data
    '''
    #Getting general news
    general_sources = get_source('business')

    print(general_sources)
    title = 'Home - Welcome to News Api'

    return render_template('index.html', title = title, general = general_sources)