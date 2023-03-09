from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from base.sql_base import Base


class Artist(Base):
    __tablename__ = 'Artists'
    id_A = Column(Integer, primary_key=True)
    name = Column(String)
    isActive = Column(String)
    songs = relationship("SongArtist", back_populates="artist")

    def __init__(self, name, isActive):
        self.name = name
        self.isActive = isActive
