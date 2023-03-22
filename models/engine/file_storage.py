#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        self.obj_types = {}
        """
        for storing classes to make instances of objects
        loaded from 'FileStorage.__file_path'.
        """

    def all(self, cls=None):
        """Returns the list of objects of one type of class"""
        if cls is None:
            return FileStorage.__objects
        else:
            new_dict = {}
            for key, value in FileStorage.__objects.items():
                if value.__class__.__name__ == cls.__name__:
                    new_dict[key] = value
            return new_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Saves storage dictionary to file"""
        objects_dict = {}
        for key, value in self.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(objects_dict, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = self.obj_types[val['__class__']](**val)
        except FileNotFoundError:
            pass
    
    def delete(self, obj=None):
        """Delete obj from __objects if it's inside, if obj is equal to None, do nothing"""
        if obj is not None:
            key = f"{type(obj).__name__}.{obj.id}"
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()
