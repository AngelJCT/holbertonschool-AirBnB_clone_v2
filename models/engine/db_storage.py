#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage():
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        """
        Constructor
        Connect to the database through self.__engine. Drop all tables if the environment variable HBNB_ENV is equal to test.
        """
        self.__engine = create_engine(
            f"mysql+mysqldb://{os.getenv('HBNB_MYSQL_USER')}:{os.getenv('HBNB_MYSQL_PWD')}@{os.getenv('HBNB_MYSQL_HOST')}/{os.getenv('HBNB_MYSQL_DB')}",
            pool_pre_ping=True,
        )
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns the list of objects of one type of class. Return a dictionary like FileStorage"""
        result = {}
        if cls is None:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = f"{type(obj).__name__}.{obj.id}"
                result[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for class_ in classes:
                objects = self.__session.query(class_).all()
                for obj in objects:
                    key = f"{type(obj).__name__}.{obj.id}"
                    result[key] = obj
        return result
    
    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)
    
    def save(self):
        """Saves storage dictionary change to file"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Delete obj from __objects if it's inside, if obj is equal to None, do nothing"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """Create current database session"""
        Base.metadata.create_all(self.__engine)  # Create all tables in the database
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
