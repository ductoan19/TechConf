import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL = os.getenv('POSTGRES_URL')
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PW = os.getenv('POSTGRES_PW')
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL

    CONFERENCE_ID = 1

    SECRET_KEY = os.getenv('SECRET_KEY')
    SERVICE_BUS_CONNECTION_STRING =os.getenv('SERVICE_BUS_CONNECTION_STRING')
    SERVICE_BUS_QUEUE_NAME = os.getenv('SERVICE_BUS_QUEUE_NAME')
    
    SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
    ADMIN_EMAIL_ADDRESS = os.getenv('ADMIN_EMAIL_ADDRESS')

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False