from datetime import datetime, timedelta

from passlib.context import CryptContext

from models import userModel
from models.userModel import User
from base.sql_base import Session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_users():
    session = Session()
    users = session.query(User).all()
    return users


def get_userId(_id: int):
    session = Session()
    user = session.query(User).filter(User.id_U == _id)
    for u in user:
        return u


def get_username(_user: str):
    session = Session()
    user = session.query(User).filter(User.username == _user)
    for u in user:
        return u


def delete_user(_id: int):
    session = Session()
    user = session.query(User).filter(User.id_U == _id).one()

    try:
        session.delete(user)
        session.commit()
    except Exception as exc:
        print(f"Failed to delete user - {exc}")


def create_user(username, password, email, phoneNumber, isAdmin):
    session = Session()

    user = User(username, password, email, phoneNumber, isAdmin)
    try:
        session.add(user)
        session.commit()
    except Exception as exc:
        print(f"Failed to add user - {exc}")
    return user





