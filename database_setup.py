import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

''' Make an instance of the declarative_base you just imported,
declarative_base shows we are using special sqlalchemy classes '''
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))



class Category(Base):
	# A variable (__tablename__)to refer to our table name
    __tablename__ = 'category'
	
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    catalog_item = relationship('CatalogItem', cascade='all, delete-orphan')


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
       }


class CatalogItem(Base):
	# A variable (__tablename__)to refer to our table name
    __tablename__ = 'catalog_item'
	
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    season = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    # Add this serialize function to be able to send JSON objects in a 
    # serializable format

    @property
    def serialize(self):

        return{
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.season,
        }




''' Make an instance of the engine class and point to 
our database '''
engine = create_engine('sqlite:///itemcatalogwithusers.db')

'''Create all tables in the engine. 
This is equivalent to "Create Table"
statements in raw SQL.Adds the classes as
 new table in the database'''
Base.metadata.create_all(engine)
