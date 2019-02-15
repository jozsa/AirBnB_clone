#!/usr/bin/python3
import uuid as uuid
from datetime import datetime
from models import storage

class BaseModel:
    """ base class model for """
    def __init__(self, *args, **kwargs):
        """ initializes class with id and created at time"""
        if kwargs:
            for key, value in kwargs.items():
                if key is 'created_at' or key is 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f") 
                elif key is '__class__':
                    value = self.__class__
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """ prints out a string representation of called instance """
        return "[{}] ({}) {}".format(
                    self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        """ updates the current instance """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """ makes instance a dictionary """
        json_dict = {}
        for key, value in self.__dict__.items():
            json_dict[key] = value
        json_dict['__class__'] = self.__class__.__name__
        json_dict['created_at'] = datetime.isoformat(self.created_at)
        json_dict['updated_at'] = datetime.isoformat(self.updated_at)
        return json_dict
