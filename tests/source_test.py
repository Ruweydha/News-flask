import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Source class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_source = Source("Cnn", "https://cnn.com", "Top news worldwide", 1)

    def test_init(self):
        self.assertEqual(self.new_source.name, "Cnn")   
        self.assertEqual(self.new_source.url, "https://cnn.com" ) 
        self.assertEqual(self.new_source.description, "Top news worldwide")
        self.assertEqual(self.new_source.id, 1)
        

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))    
