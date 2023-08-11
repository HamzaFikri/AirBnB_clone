#!/usr/bin/python3
"""
Here you can find the class State
"""

from models.base_model import BaseModel


class State(BaseModel):
    """here start the class State"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the class State"""
        name = ""

        super().__init__(*args, **kwargs)
