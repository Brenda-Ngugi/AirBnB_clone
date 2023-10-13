#!/usr/bin/python3
"""
Imported Modules
BaseModel
"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """
    Store city and state id
    params:
       state_id: string - empty string: it will be the State.id
       name: string - empty string
    """
    state_id = ""
    name = ""
