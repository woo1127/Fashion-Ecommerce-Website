import os
import hashlib
from utils import get_base_dir


basedir = get_base_dir()


class Config(object):

    FLASK_APP = 'app.py'
    SECRET_KEY = os.environ.get('SECRET_KEY', hashlib.sha256("FashionEcommerce".encode('utf-8')).hexdigest())
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    WHOOSH_INDEX_PATH = os.environ.get('WHOOSH_INDEX_PATH', os.path.join(basedir, 'indexdir'))
    PRODUCTS_PER_PAGE = 28
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', '9f3lJrckaV2EPiC403XhXSgkbRA2V1LPRkGLad6ZqpdFa2DRPbLIQG7Sej6eAyD')
    JWT_TOKEN_LOCATION = ['cookies', 'headers']
    JWT_SESSION_COOKIE = False


class ProuctionConfig(Config):

    DEBUG = False
    ENV = 'production'
    JWT_COOKIE_SECURE = True
    JWT_COOKIE_EXPIRES = 60 * 60 * 24 * 90 # 90 days
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 60 * 24 * 90 # 90 days


class DevelopmentConfig(Config):

    DEBUG = True
    ENV = 'development'
    JWT_COOKIE_SECURE = False
    JWT_COOKIE_EXPIRES = 60 * 60 * 24 * 1 # 1 day
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 60 * 24 * 1 # 1 day
