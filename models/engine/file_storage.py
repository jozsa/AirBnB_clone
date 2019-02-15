#!/usr/bin/python3
"""
This module has one class: FileStorage
FileStorage will be able to serialize instances
to JSON file & deserialize JSON file to instances
"""
import models
import json

class FileStorage:
    """
    """
    def __init__(self):
        """ """
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets 'obj' in __objects with key <obj class name>.id """
        self.key = obj.__class__.__name__ + '.' + obj.id
        self.__objects = {self.key:obj}

    def save(self):
        """ Serializes __objects to JSON file """
        for key, value in self.__objects.items():
            self.__objects[key] = value.to_dict()
        print(self.__objects)
        with open(self.__file_path, mode='a+', encoding='utf-8') as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        """Deserializes JSON file to __objects if file path exists"""
        try:
            with open(self.__file_path, encoding='utf-8') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            pass
