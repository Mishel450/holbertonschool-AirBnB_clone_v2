#!/usr/bin/python3
"""db_storage"""
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel
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
        self.__engine = create_engine('mysql+myswqldb://{}:{}@{}:3306/{}'
                           .format(user, password, host, database), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(self.__engine)
        self.__session = Session()

        if env == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """query on the current database session """
        pass

    def new(self, obj):
        """add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

