#!/usr/bin/python3
"""
You can find the base model function here
"""

import models
import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Here start the BaseModel function"""
    def __init__(self, *args, **kwargs):
        """ here init the function """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Function that prints class name, id and __dic"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Function that updates the public instance attribute
updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of dict
 of the instance """
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
