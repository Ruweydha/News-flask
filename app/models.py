class Source:
    '''
    Source class to define source objects
    '''
    def __init__(self, name, url, description, id):
        self.name = name
        self.id = id
        self.url = url
        self.description = description

class News:
    def __init__(self, author, content, title, url, urlToImage, publishedAt ):
        self.author = author
        self.description = content 
        self.title = title
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt