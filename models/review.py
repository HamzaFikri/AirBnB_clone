#!/usr/bin/python3
"""
Here you can find the class Review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Here start the class Review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize the class Review"""
        super().__init__(*args, **kwargs)
