#!/usr/bin/env python3
"""
uuid module - create a unique id for BaseModel
datetime module - create current time
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    def __init__(self, *args, **kwargs):
        """ initialize public instance attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime
                            (value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """return string representation for the object of the class"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id,
                                      self.__dict__))

    def save(self):
        """update the updated_at with the last save"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """return a dictionary with keys/values of an instance
           loop through self.__dict__
        """
        new_dict = {}
        for key, value in self.__dict__.items():
            new_dict[key] = value.isoformat() if "_at" in key else value
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
