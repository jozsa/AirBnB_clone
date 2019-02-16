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
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets 'obj' in __objects with key <obj class name>.id """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to JSON file """
        for key, value in FileStorage.__objects.items():
            if not isinstance(value, dict):
                FileStorage.__objects[key] = value.to_dict()
        with open(FileStorage.__file_path,
                  mode='w+', encoding='utf-8') as json_file:
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        """Deserializes JSON file to __objects if file path exists"""
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as json_file:
                FileStorage.__objects = json.load(json_file)
            for value in FileStorage.__objects.values():
                value = self.new(BaseModel(**value))
        except FileNotFoundError:
            pass
