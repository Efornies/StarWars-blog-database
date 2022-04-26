import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    name =Column(String (250))
    lastname = Column(String(250))
    password = Column(String(250))
    email =Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name =  Column(String(250), nullable=False)
    description = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    eye_color = Column(Integer)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    population = Column(String(250))
    terrain = Column(String(250))
    gravity = Column(Integer)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    passengers = Column(String(250))
    cargo_capacity = Column(String(250))
    consumibles = Column(Integer)
   
    
class Favourite(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    Favourite_user=Column(Integer, ForeignKey("user.id"))
    Favourite_planets=Column(Integer, ForeignKey("planets.id"))
    Favourite_characters=Column(Integer, ForeignKey("characters.id"))
    Favourite_vehicles=Column(Integer, ForeignKey("vehicles.id"))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')