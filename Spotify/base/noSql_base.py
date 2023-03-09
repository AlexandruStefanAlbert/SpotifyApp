from pymongo import MongoClient
from bson.objectid import ObjectId

# check uri string to add user and password

steam_users_client = MongoClient("mongodb://admin:passwdadmin@192.168.56.20:27017/admin")
steam_users_db = steam_users_client["playlists"]


class Playlist:
    def __init__(self, user_dict):
        self.id = user_dict['_id']
        self.title = user_dict['title'] if 'title' in user_dict else None
        self.artist = user_dict['artist'] if 'artist' in user_dict else None

    def __iter__(self):
        for attr, value in self.__dict__.items():
            if value is not None:
                yield attr, value

    def __str__(self):
        return "".join([f"{field} = {value} " for field, value in self.__iter__()])
