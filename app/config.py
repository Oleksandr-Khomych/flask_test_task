import os
from dotenv import load_dotenv


load_dotenv()


class Configuration(object):
    DEBUG = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    # Щоб не виводило попередження при запуску сервера
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    # DATABASE = '/database.db'

    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
