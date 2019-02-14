#!/usr/bin/python3
import uuid as uuid
from datetime import datetime

class BaseModel:
    """ base class model for """
    def __init__(self, id=None, created_at=0, updated_at=0):
        """ initializes class with id and created at time"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """ prints out a string representation of called instance """
        return "[{}] ({} <{}>".format(
                        'BaseModel', self.id, self.__dict__)
    def save(self):
        """ updates the current instance """
        self.updated_at = datetime.today()

    def to_dict(self):
        """ makes instance a dictionary """
        self.__dict__['__class__'] = 'BaseModel'
        self.__dict__['created_at'] = datetime.isoformat(self.created_at)
        self.__dict__['updated_at'] = datetime.isoformat(self.updated_at)
        return self.__dict__

