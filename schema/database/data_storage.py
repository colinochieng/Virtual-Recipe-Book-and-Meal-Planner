#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from schema.recipe import Base
from schema.user import User
from schema.recipe import Recipe


class DataDriver:
    url = 'mysql+mysqldb://recipe:recipe_pwd@localhost/virtual_recipe_meal'
    
    def __init__(self):
        self.__driver = create_engine(self.url, pool_pre_ping=True)
        self.__session = None

    def restart(self):
        Base.metadata.create_all(self.__driver)
        Session = sessionmaker(bind=self.__driver, expire_on_commit=False)
        Scoped = scoped_session(session_factory=Session)
        self.__session = Scoped()
    

    def new(self, data):
        self.__session.add(data)
    
    def save(self):
        self.__session.commit()

    def get_user_by_email(self, cls, email):
        return self.__session.query(cls).filter(cls.email == email).one_or_none()

    def close(self):
        self.__session.close()

storage = DataDriver()
storage.restart()
