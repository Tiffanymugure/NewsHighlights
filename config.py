import os

class Config:
    
    NEWS_SOURCES_BASE_URL=''
    ARTICLES_BASE_URL =''

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    DEBUG = True

# class Config:
#     '''
#     General configuration parent class
#     '''
#     SOURCES_API_BASE_URL ='https://api.thenewsdb.org/3/news/{}?api

config_options ={
    'development':DevConfig,
    'production':ProdConfig
}