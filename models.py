from sqlalchemy import Column, String, Integer
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(8))
    comments = Column(String(120), default=" ")


    def change_name(self, new_name):
        self.name = new_name


    def __init__(self, name=None, email=None, password=None, comments=None):
        self.name = name
        self.email = email
        self.password = password
        self.comments = comments

    def __repr__(self):
        return "<User %s>" % (self.name)
