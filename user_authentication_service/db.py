#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Save the user to the database"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """find user method"""
        session = self._session
        try:
            results = session.query(User).filter_by(**kwargs).first()
            if not results:
                raise NoResultFound
            return results
        except InvalidRequestError:
            raise

    def update_user(self, user_id: int, **kwargs) -> None:
        """update data for user"""
        session = self._session
        updated_user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(updated_user, key):
                raise ValueError
            setattr(updated_user, key, value)
        session.commit()
