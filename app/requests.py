from distutils.file_util import move_file
from unicodedata import name
import urllib.request, json
from .models import Source

#getting Api key
api_key = None

#getting the news base url
base_url = None

def configure_request(app):
    global api_key, base_url

    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_source(category):
    get_source_url = f'{base_url}top-headlines/sources/?apiKey={api_key}'

    with urllib.request.urlopen(get_source_url)  as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results        


def process_results(source_list):
    source_results = []   
    for source_item in source_list:
        name = source_item.get('name') 
        url =   source_item.get('url')
        description = source_item.get('description')
        id = source_item.get('id')

    
        source_object = Source(name, url, description, id)
        source_results.append(source_object)

    return  source_results