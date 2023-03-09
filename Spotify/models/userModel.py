from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base.sql_base import Base
from models.users_rolesModel import UsersRoles


class User(Base):
    __tablename__ = 'Users'
    id_U = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    phoneNumber = Column(Integer)
    isAdmin = Column(String)

    roles = relationship("UsersRoles", back_populates="user")

    def __init__(self, _username, _password, _email, _phoneNumber, _isAdmin):
        self.username = _username
        self.password = _password
        self.email = _email
        self.phoneNumber = _phoneNumber
        self.isAdmin = _isAdmin
