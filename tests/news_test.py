import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_news_article = News("Ruweydha","Hackathon has began", "Hackathon in kenya has began" "https://cnn.com", "imageurl", "21st January, 2022")
        
    def test_init(self):
        self.assertEqual(self.new_news_article.author, 'Ruweydha')
        self.assertEqual(self.new_news_article.content, "Hackathon has began")
        self.assertEqual(self.new_news_article.title, "Hackathon in kenya has began")
        self.assertEqual(self.new_news_article.url, "https://cnn.com")
        self.assertEqual(self.new_news_article.urlToImage, "imageurl")
        self.assertEqual(self.new_news_article.publishedAt, "21st January, 2022")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_article, News))    
    

