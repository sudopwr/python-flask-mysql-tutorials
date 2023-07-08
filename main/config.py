import os


class ProductionConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    JWT_SECRET = os.getenv("JWT_SECRET")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")


class DevelopmentConfig:
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    JWT_SECRET = os.getenv("JWT_SECRET")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")

config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
