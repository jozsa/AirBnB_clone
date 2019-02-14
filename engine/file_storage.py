#!/usr/bin/python3
"""
This module has one class: FileStorage
FileStorage will be able to serialize instances
to JSON file & deserialize JSON file to instances
"""
from models.base_model import BaseModel
import json

class FileStorage:
    """
    """
    self.__file_path = 'file.json'
    self.__objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets 'obj' in __objects with key <obj class name>.id """
        

    def save(self):
        """ Serializes __objects to JSON file """
        with open(self.__file_path, mode='w+', encoding='utf-8') as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        """ Deserializes JSON file to __objects if file path exists"""
        with open(self.__file_path, encoding='utf-8') as json_file:
            self.__objects = json.load(json_file)
