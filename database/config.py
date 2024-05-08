import os

from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Config:
    DEBUG = False
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB = os.getenv('MYSQL_DB')
    MYSQL_CURSORCLASS = 'DictCursor'
