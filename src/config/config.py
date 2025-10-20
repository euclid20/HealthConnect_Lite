import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    CONFIG_MODE = os.getenv("CONFIG_MODE", "development")
    SQLALCHEMY_DATABASE_URI = os.getenv(f"{CONFIG_MODE.upper()}_DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
