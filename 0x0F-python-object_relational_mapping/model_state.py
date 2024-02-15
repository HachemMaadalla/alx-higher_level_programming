#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, text
"""
    Module that performs creates a States class based off of Base.
"""
Base = declarative_base()


class State(Base):
    """
        The ``States`` class which inherits from ``Base`` class.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
