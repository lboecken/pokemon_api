import os

class BaseConfig():
    SECRET_KEY=os.getenv("SECRET_KEY")
    TESTING=False

class DevelopmentConfig(BaseConfig):
    DATABASE_URI=os.getenv('DATABASE_URI')

class ProductionConfig(BaseConfig):
    DATABASE_URI=os.getenv('DATABASE_URI')