#!/usr/bin/python3
import uuid as uuid
from datetime import datetime

class BaseModel:
    """ base class model for """
    def __init__(self, *args, **kwargs):
        """ initializes class with id and created at time"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """ prints out a string representation of called instance """
        return "[{}] ({}) {}".format(
                    self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        """ updates the current instance """
        self.updated_at = datetime.today()

    def to_dict(self, **kwargs):
        """ makes instance a dictionary """
        for key, value in kwargs.items():
            if key is 'created_at' or key is 'updated_at':
                value = datetime(value)
            setattr(self, key, value)
        return self.__dict__

