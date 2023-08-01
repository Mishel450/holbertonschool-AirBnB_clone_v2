#!/usr/bin/python3
"""db_storage"""
import sqlalchemy
from sqlalchemy import create_engine
from models.base_model import Base
import os


class DBStorage:
    """the class DBStorage"""

    __engine = None
    __session = None

    

    def __init__(self):
        user = os.environ['HBNB_MYSQL_USER']
        password = os.environ['HBNB_MYSQL_PWD']
        host = os.environ['HBNB_MYSQL_HOST']
        database = os.environ['HBNB_MYSQL_DB']
        env = os.environ['HBNB_ENV']
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                           .format(user, password, host, database), pool_pre_ping=True)
        if env == "test":
            Base.metadata.create_all(self.__engine)
            Base.metadata.drop_all(self.__engine)