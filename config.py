# from instance.config import NEWS_API_KEY
import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/'

class ProdConfig(Config):
    '''
    Production Configuration class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class 
    '''
    DEBUG = True

config_options = {
    'development' : DevConfig,
    'production' : ProdConfig
}