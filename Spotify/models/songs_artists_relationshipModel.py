from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship

from base.sql_base import Base


class SongArtist(Base):
    __tablename__ = 'SongArtist'
    id = Column(Integer, primary_key=True)
    id_Song = Column(Integer, ForeignKey("Songs.id_S"))
    id_Artist = Column(Integer, ForeignKey("Artists.id_A"))

    artist = relationship("Artist", back_populates="songs")
    song = relationship("Song", back_populates="artists")

    def __init__(self, id_s, id_a):
        self.id_Song = id_s
        self.id_Artist = id_a


