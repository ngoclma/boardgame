import os

class Config:
    """
    Base configuration for the Flask app.
    """
    SECRET_KEY = 'your_secret_key'  # Change this to a random secret key for your app
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """
    Configuration for development environment.
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    DEBUG = True

class ProductionConfig(Config):
    """
    Configuration for production environment.
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = False
