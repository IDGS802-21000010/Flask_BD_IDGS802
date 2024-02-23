import os
from sqlalchemy import create_engine

class Config(object):
    SELECT_KEY='CLAVE SECRETA'
    SESSION_COOKIES_SECURE=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymsql://cardiel:root@127.0.0.1/bdidgs802'