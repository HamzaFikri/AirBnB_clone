#!/usr/bin/python
"""
Here you can find the class amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Here start the class Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes the class Amenity"""
        super().__init__(*args, **kwargs)
