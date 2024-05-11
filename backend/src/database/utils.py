import sqlalchemy_utils

from src.database.config import config


def create_database():
    if sqlalchemy_utils.database_exists(config.engine.url):
        return print(f'database {config.engine.url.database} exist.')

    sqlalchemy_utils.create_database(config.engine.url)
    return print(f'database {config.engine.url.database} created.')
