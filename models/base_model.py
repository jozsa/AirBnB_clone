#!/usr/bin/python3
"""
This module has one class: BaseModel
BaseModel will act as the base class
for all future sub-classes of the
AirBnB clone.
"""
import uuid as uuid
from datetime import datetime
import models


class BaseModel:
    """ base class model for AirBnB objects

    Attributes:
        id: str, unique UUID of instance
        created_at: datetime, time of instance creation
        updated_at: datetime, instance update time
    """
    def __init__(self, *args, **kwargs):
        """ initializes class with id and created at time"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = \
                        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """ prints out a string representation of called instance """
        return "[{}] ({}) {}".format(
                    self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the current instance """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ makes instance a dictionary """
        json_dict = {}
        for key, value in self.__dict__.items():
            json_dict[key] = value
        json_dict['__class__'] = self.__class__.__name__
        json_dict['created_at'] = self.created_at.isoformat()
        json_dict['updated_at'] = self.updated_at.isoformat()
        return json_dict
