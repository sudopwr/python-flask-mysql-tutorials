import os


class ProductionConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")


class DevelopmentConfig:
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
