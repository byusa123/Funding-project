import os

class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynt:zion@localhost/gofund'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynt:zion@localhost/gofund_test'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://cynt:zion@localhost/gofund'
    DEBUG = True

config_options = {
    'test' : TestConfig,
    'development' : DevConfig,
    'production' :ProdConfig
}