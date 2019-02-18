#!/usr/bin/python3
"""
This module has one class: User
inherited from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
