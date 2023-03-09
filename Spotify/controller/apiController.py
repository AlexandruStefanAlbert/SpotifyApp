from datetime import datetime, timedelta
from http.client import HTTPException
from typing import Union

from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy import false
from jose import jwt
from starlette import status
from starlette.middleware.cors import CORSMiddleware

from models.songModel import Gen
from models.userModel import User
from base.noSql_base import steam_users_db, Playlist
# from repository.artist_repository import get_artist
from repository.artist_repository import create_artist, get_artist, delete_artist, get_artistId, get_artistName, \
    update_artist
from repository.role_repository import get_roles, create_role
from repository.song_artist_repository import create_song_artist, get_song_artist_id
from repository.songs_repository import get_songs, create_song, get_songId, delete_song, get_songName, update_song
# from repository.songs_repository import create_song, get_songs
from repository.user_repository import create_user, get_users, delete_user, get_username, get_userId
import uvicorn

# Press the green button in the gutter to run the script.

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str


class LoginModel(BaseModel):
    username: str
    password: str


class TokenData(BaseModel):
    username: Union[str, None] = None


def verify_password(plain_pass, hashed_pass):
    return pwd_context.verify(plain_pass, hashed_pass)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate(_username: str, _pass: str):
    user = get_username(_username)
    if not user:
        return False
    if not verify_password(_pass, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("sub")
    if username is None:
        return False
    token_data = TokenData(username=username)

    user = get_username(token_data.username)

    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    content = {"acces_token": access_token}
    response = JSONResponse(content=content)
    response.set_cookie(key="acces_token", value=access_token)
    # payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
    # username: str = payload.get("sub")
    # print(username)
    # user = get_username(username)

    return response
    # return {"access_token": access_token, "token_type": "bearer"}


@app.get("/user/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    print(current_user.username)


@app.post('/users')
async def create_users(_username: str, _password: str, _email: str, _phoneNumber: int, _isAdmin: str):
    user = create_user(username=_username, password=pwd_context.hash(_password), email=_email, phoneNumber=_phoneNumber,
                       isAdmin=_isAdmin)
    return user


@app.get('/users')
def users_list():
    return get_users()



@app.get('/users/{user_id}')
def get_user_by_Id(user_id: int):
    user = get_userId(user_id)
    return get_username(user.username)

    #return {"User": get_userId(user_id)}





@app.get('/user/{username}')
def get_user_by_username(_username: str):
    return {"User:": get_username(_username)}


@app.delete('/users/{user_id}')
def delete_User(user_id: int):
    delete_user(user_id)


@app.get('/roles')
def roles_list():
    return {"Roles ": get_roles()}


@app.post('/roles')
def create_roles(role: str):
    role = create_role(value=role)
    return role


@app.post('/songs')
async def create_songs(_title: str, _genMuzical: Gen, _anAparitie: str):
    song = create_song(title=_title, genMuzical=_genMuzical, anAparitie=_anAparitie)
    return song


@app.post('/songs/{song_id}')
async def update_Song(song_id: int, _title: str, _genMuzical: Gen, _anAparitie: str):
    song = update_song(id=song_id, title=_title, genMuzical=_genMuzical, anAparitie=_anAparitie)
    return song


@app.get('/songs')
def songs_list():
    return get_songs()


@app.get('/songs/{song_id}')
def user_detail(song_id: int):
    return get_songId(song_id)


@app.delete('/songs/{song_id}')
def delete_Song(song_id: int):
    delete_song(song_id)


@app.get('/artists')
def artists_list():
    return get_artist()


@app.get('/artists/{artist_id}')
def get_artist_by_id(artist_id: int):
    return get_artistId(artist_id)


@app.get('/artist/{artist_name}')
def get_artist_by_Name(artist_name: str):
    return {"Artist": get_artistName(artist_name)}


@app.post('/artists')
async def create_artists(_name: str, _isActive: str):
    artist = create_artist(name=_name, isActive=_isActive)
    return artist


# update artist
@app.post('/artists/{artist_id}')
async def update_Artist(_artist_id: int, _name: str, _isActive: str):
    artist = update_artist(id=_artist_id, name=_name, isActive=_isActive)
    return artist


@app.delete('/artists/{artist_id}')
def delete_Artist(artist_id: int):
    delete_artist(artist_id)


@app.post('/collection')
def create_Collection(song_id: int, artist_id: int):
    collection = create_song_artist(id_Song=song_id, id_Artist=artist_id)
    return collection


# melodiile artistului cu id-ul artist_id
@app.get('/collections/{artist_id}/song')
async def get_artist_song(artist_id: int):
    collection = get_song_artist_id(artist_id)
    artist = get_artistId(artist_id)
    title = []
    for a in collection:
        #for art in artist:
        title.append("Title: " + a.title + " - " + artist.name + ", an " + a.anAparitie)
    return title



@app.post('/playlist')
def create_Playlist(_playlist: str, _song: str, _artist: str):
    collectionExist = steam_users_db.list_collection_names().__contains__(_playlist)
    if collectionExist == false:
        steam_users_db.create_collection(_playlist)
    else:
        playlist_collection = steam_users_db[_playlist]

    song = get_songName(_song)
    artist = get_artistName(_artist)

    playlist = {
        "title": song.title,
        "artist": artist.name
    }
    playlist_collection.insert_one(playlist)


@app.get('/playlist/{playlist_name}')
def show_Playlist(_playlist: str):
    playlist = steam_users_db[_playlist]
    songs_list = [Playlist(song) for song in playlist.find({})]
    song = []
    for s in songs_list:
        song.append(s.__str__() )
    return '\n'+song.__str__()

