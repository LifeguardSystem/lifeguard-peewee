"""
Connection methods implementations
"""
from peewee import MySQLDatabase

from lifeguard_peewee.settings import (
    LIFEGUARD_PEEWEE_DBMS_NAME,
    LIFEGUARD_PEEWEE_HOST,
    LIFEGUARD_PEEWEE_PORT,
    LIFEGUARD_PEEWEE_USER,
    LIFEGUARD_PEEWEE_PASSWORD,
    LIFEGUARD_PEEWEE_DATABASE,
)


class DatabaseNotImplementedException(Exception):
    """
    Notify invalid option for DMBS
    """


def connection_factory():
    """
    Return database
    """

    database = None

    if LIFEGUARD_PEEWEE_DBMS_NAME == "mysql":
        database = MySQLDatabase(
            LIFEGUARD_PEEWEE_DATABASE,
            user=LIFEGUARD_PEEWEE_USER,
            password=LIFEGUARD_PEEWEE_PASSWORD,
            host=LIFEGUARD_PEEWEE_HOST,
            port=LIFEGUARD_PEEWEE_PORT,
        )
    else:
        raise DatabaseNotImplementedException(LIFEGUARD_PEEWEE_DBMS_NAME)

    database.connect()

    return database
