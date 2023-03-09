from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("mariadb+pymysql://administrator:administrator@192.168.56.10:3306/Spotify")
Session = sessionmaker(bind=engine)