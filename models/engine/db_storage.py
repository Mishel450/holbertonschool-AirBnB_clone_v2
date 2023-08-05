#!/usr/bin/python3
"""db_storage"""
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import relationship

from os import getenv


class DBStorage:
    """the class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+myswqldb://{}:{}@{}/{}'
                           .format(user, password, host, database), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """query on the current database session """
        from models.city import City
        from models.state import State
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        
        the_dict = {}
        
        if cls is None:
            query = self.__session.query(
                User, State, City, Amenity, Place, Review).all()
        else:
            query = self.__session.query(cls).all()
        for i in query:
            the_dict[i.__class__.__name__ + '.' + i.id] = i
        return the_dict


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
        the_session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        Session = scoped_session(the_session)
        self.__session = Session()
    cities = relationship('City', backref='state', cascade='all, delete-orphan')