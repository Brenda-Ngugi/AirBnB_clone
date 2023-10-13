#!/usr/bin/python3
"""
Imported modules:
BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    The name of the amenity
    params:
      name: string - empty string
    """
    name = ""
