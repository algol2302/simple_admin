import os


class Config(object):
    user = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    host = os.environ['POSTGRES_HOST']
    database = os.environ['POSTGRES_DB']
    port = os.environ['POSTGRES_PORT']

    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')

    SQLALCHEMY_DATABASE_URI = (
        f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
