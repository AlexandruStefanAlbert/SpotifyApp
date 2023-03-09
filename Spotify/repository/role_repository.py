from base.sql_base import Session
from models.roleModel import Role


def get_roles():
    session = Session()
    roles = session.query(Role).all()
    return roles

def create_role(value:str):
    session = Session()
    role = Role(value)

    try:
        session.add(role)
        session.commit()
    except Exception as exc:
        print(f"Failed to add role - {exc}")
    return role