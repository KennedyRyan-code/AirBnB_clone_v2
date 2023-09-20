#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import column, string


class User(BaseModel, Base):
    """ User Representation """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128),
                       nullable=False)
        password = Column('password',
                           String(128),
                           nullable=False)
        first_name = Column(String(128),
                            nullable=True)
        last_name = Column(String(128),
                           nullable=True)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
