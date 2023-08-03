#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from models import storage
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
   
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

    def cities(self):
        from models import storage
        result = []
        for city in storage.all('City').values():
            if self.id == city.state_id:
                result.append(city)
        return result
