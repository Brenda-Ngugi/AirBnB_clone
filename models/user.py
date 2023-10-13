#!/usr/bin/python3
"""
Imported Modules:
BaseModel
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class User(BaseModel):
    """
    User class inherits from BaseModel.
    params:
       email: string - empty string
       password: string - empty string
       first_name: string - empty string
       last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
