#!/usr/bin/python3
"""Definition of a state class"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

connection = engine.connect()

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
