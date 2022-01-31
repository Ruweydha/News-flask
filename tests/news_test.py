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
        self.new_news_article = News("Ruweydha","Hackathon has began", "Hackathon in kenta has began" "https://cnn.com", "imageurl", "21st January, 2022")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_article, News))    


