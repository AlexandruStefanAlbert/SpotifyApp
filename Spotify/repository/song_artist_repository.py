from base.sql_base import Session
from models.artistModel import Artist
from models.songModel import Song
from models.songs_artists_relationshipModel import SongArtist
from repository.songs_repository import get_songId


def get_song_artist():
    session = Session()
    songs_artist = session.query(SongArtist)
    return songs_artist


def get_song_artist_id(uuid: int):
    session = Session()
    songs = session.query(Song).filter(SongArtist.id_Song == Song.id_S).filter(SongArtist.id_Artist == uuid).all()
    return songs



def create_song_artist(id_Song, id_Artist):
    session = Session()
    song_artist = SongArtist(id_Song, id_Artist)
    try:
        session.add(song_artist)
        session.commit()
    except Exception as exc:
        print(f"Failed to add song-artist -{exc}")
    return song_artist
