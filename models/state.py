#!/usr/bin/python3
"""
This module has one class: State
inherited from BaseModel
"""
from models.base_mdoel import BaseModel


class State(BaseModel):
    """State class:

    Attributes:
        name: str, state name
    """
    name = ''
