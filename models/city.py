#!/usr/bin/python
"""
Here you can find the clas City
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Here start the class City"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initialize the class city"""
        super().__init__(*args, **kwargs)
