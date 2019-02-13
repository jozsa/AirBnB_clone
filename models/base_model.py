#!/usr/bin/python3
import uuid as uuid
from datetime import datetime

class BaseModel:
    """ base class model for """
    def __init__(self):
        """ initializes class with id and created at time"""
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """ prints out a string representation of called instance """
        return ("[{}] ({} <{}>".format(
                        self.__class__, self.id, self.__dict__)
    def save(self):
        """ updates the current instance """
        return self.updated_at = updated_at()


    @property
    def id(self):
        return self.id

    @id.setter
    def id(self):
        self.id = str(uuid.uuid4())

    @property
    def created_at(self):
        return self.updated_at()

    @created_at.setter
    def created_at(self):
        self.created_at = datetime.today()

    @property
    def updated_at(self):
        return self.updated_at()
    @updated_at.setter
    def updated_at(self):
        self.updated_at = datetime.today()
