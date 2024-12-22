#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User
import user


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    """ Task 2"""

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a user to the database.

        Args:
            email (str): The user's email address.
            hashed_password (str): The user's hashed password.

        Returns:
            User: The created User object.
        """
        se = self._session
        user = User(email=email, hashed_password=hashed_password)
        se.add(user)
        se.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """This method should take in arbitrary keyword arguments and return
        the first row found in the users table as filtered by these arguments.
        """
        sess = self._session
        try:
            return sess.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound
        except InvalidRequestError:
            raise InvalidRequestError

    """ Task 3"""

    def update_user(self, user_id: int, **kwargs) -> None:
        """This method should take a required integer user_id argument and
        arbitrary keyword arguments, and update the users table record with
        the corresponding user_id.

        Args:
            user_id (int): The user ID.
        """
        session = self._session
        try:
            session.query(User).filter_by(id=user_id).update(kwargs)
            session.commit()
            return None
        except ValueError:
            raise ValueError
