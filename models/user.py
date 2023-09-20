#!/usr/bin/python3
"""This module defines a class User"""

from models.base_model import BaseModel, Base
import models


class User(BaseModel, Base):
    """ User Representation """

    __tablename__ = 'users'
    email = Column(String(128),
                   nullable=False)
    password = Column(String(128),
                      nullable=False)
    first_name = Column(String(128),
                        nullable=True)
    last_name = Column(String(128),
                       nullable=True)
