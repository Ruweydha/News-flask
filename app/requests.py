from distutils.file_util import move_file
from unicodedata import name
import urllib.request, json
from .models import Source, News
from dateutil.parser import isoparse
from dateutil.tz import UTC

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

def process_results2(articles_list):
    articles_results =[]
    for article_item in articles_list:
         author = article_item.get('author')
         title = article_item.get('title')
         content = article_item.get('content')
         article_url = article_item.get('url')
         urlToImage = article_item.get('urlToImage')
         publishedAt = article_item.get('publishedAt')

         date_published=isoparse(publishedAt)
         date_published.astimezone(UTC)
         new_publication_date=date_published.strftime("%b %d, %Y %H:%M:%S")
          
         if urlToImage and content and article_url: 
            articles_object = News(author, content, title, article_url, urlToImage, new_publication_date)
            articles_results.append(articles_object)    

    return articles_results        

def view_source(id):
    get_source_articles_url = f'{base_url}top-headlines?sources={id}&apiKey={api_key}'  

    with urllib.request.urlopen(get_source_articles_url) as url:
        source_details_data =  url.read()
        source_articles_response = json.loads(source_details_data)

        source_articles = None

        if source_articles_response['articles'] :
            source_articles_list = source_articles_response['articles'] 
            source_articles = process_results2(source_articles_list)  

    return source_articles

def view_category(category):
    view_category_url = f"{base_url}top-headlines?category={category}&apiKey={api_key}"
    with urllib.request.urlopen(view_category_url) as url:
        category_details_data = url.read()
        category_articles_response = json.loads(category_details_data)

        category_articles = None

        if category_articles_response['articles']:
         category_articles_list = category_articles_response['articles'] 
         category_articles = process_results2(category_articles_list)
    print(category_articles)
    return category_articles     

