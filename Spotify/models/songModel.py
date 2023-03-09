import enum

import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base.sql_base import Base
from enum import Enum
import datetime


class Gen(enum.Enum):
    rock = 'rock'
    rap = 'rap'
    pop = 'pop'


class Song(Base):
    __tablename__ = 'Songs'
    id_S = Column(Integer, primary_key=True)
    title = Column(String)
    genMuzical = Column(sqlalchemy.Enum(Gen))
    anAparitie = Column(String)

    artists = relationship("SongArtist", back_populates="song")

    def __init__(self, title, gen, an):
        self.title = title
        self.genMuzical = gen
        self.anAparitie = an
