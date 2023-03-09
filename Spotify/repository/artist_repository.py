from models.artistModel import Artist
from base.sql_base import Session


def get_artist():
    session = Session()
    artists = session.query(Artist).all()
    return artists


def get_artistId(_id: int):
    session = Session()
    artist = session.query(Artist).filter(Artist.id_A == _id)
    for a in artist:
        return a


def get_artistName(_name: str):
    session = Session()
    artist = session.query(Artist).filter(Artist.name == _name)
    for a in artist:
        return a


def delete_artist(_id: int):
    session = Session()
    artist = session.query(Artist).filter(Artist.id_A == _id).one()

    try:
        session.delete(artist)
        session.commit()
    except Exception as exc:
        print(f"Failed to delete artist - {exc}")


def update_artist(id, name, isActive):
    session = Session()
    _artist = session.query(Artist).filter(Artist.id_A == id)
    for a in _artist:
        a.name = name
        a.isActive = isActive
        try:
            session.commit()
            session.refresh(a)
        except Exception as exc:
            print(f"Failet to update artist = {exc}")
        return a


def create_artist(name, isActive):
    session = Session()
    artist = Artist(name, isActive)
    try:
        session.add(artist)
        session.commit()
    except Exception as exc:
        print(f"Failed to add artist - {exc}")
    return artist
