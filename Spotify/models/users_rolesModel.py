from sqlalchemy import Table, Integer, ForeignKey, Column
from sqlalchemy.orm import relationship

from base.sql_base import Base


class UsersRoles(Base):
    __tablename__ = 'UsersRoles'
    id_UR = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Users.id_U"))
    role_id = Column(Integer, ForeignKey("Roles.id_R"))

    role = relationship("Role", back_populates="users")
    user = relationship("User", back_populates="roles")


    def __init__(self, id_User, id_Role):
        self.user_id = id_User
        self.role_id = id_Role
