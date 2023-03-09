from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship


from base.sql_base import Base
from models.users_rolesModel import UsersRoles


class Role(Base):
    __tablename__ = 'Roles'
    id_R = Column(Integer, primary_key=True)
    value = Column(String)

    users = relationship("UsersRoles", back_populates="role")

    def __init__(self, value):
        self.value = value
