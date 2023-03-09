from models.songModel import Song
from base.sql_base import Session
from models.songs_artists_relationshipModel import SongArtist


def get_songs():
    session = Session()
    songs = session.query(Song).all()
    return songs


def get_songId(_id: int):
    session = Session()
    song = session.query(Song).filter(Song.id_S == _id)
    for s in song:
        return s


def get_songName(_name: str):
    session = Session()
    song = session.query(Song).filter(Song.title == _name)
    for s in song:
        return s

def update_song(id, title, genMuzical, anAparitie ):
    session = Session()
    _song = session.query(Song).filter(Song.id_S==id)
    for s in _song:
        s.title=title
        s.genMuzical=genMuzical
        s.anAparitie=anAparitie
        try:
            session.commit()
            session.refresh(s)
        except Exception as exc:
            print(f"Failed to update artist = - {exc}")
        return s
def delete_song(_id: int):
    session = Session()
    song = session.query(Song).filter(Song.id_S == _id).one()

    try:
        session.delete(song)
        session.commit()
    except Exception as exc:
        print(f"Failed to delete song - {exc}")


def create_song(title, genMuzical, anAparitie):
    session = Session()
    song = Song(title, genMuzical, anAparitie)
    try:
        session.add(song)
        session.commit()
    except Exception as exc:
        print(f"Failed to add song - {exc}")
    return song
