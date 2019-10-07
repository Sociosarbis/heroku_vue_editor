import os
from urllib.parse import urlparse
from sqlalchemy import create_engine, Table, Column, Integer, String, Text, ForeignKey, Binary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

DEFAULT_DATABASE_URL = f"//postgres:Pg_music71016@{os.getenv('DB_HOST', 'localhost')}:5432/heroku_app"
DATABASE_URL = os.getenv('DATABASE_URL', DEFAULT_DATABASE_URL)
engine = create_engine(
  urlparse(DATABASE_URL)
    ._replace(scheme='postgresql+psycopg2')
    .geturl(),
  connect_args={'sslmode': 'allow'},
  echo=True
)

Session = sessionmaker(bind=engine)
Base = declarative_base()


class User_English_link(Base):
  __tablename__ = 'user_English_link'
  user_id = Column('user_id', ForeignKey('user.id'), primary_key=True)
  English_id = Column('English_id', ForeignKey('English.id'), primary_key=True)
  tag_name = Column('tag_name', ForeignKey('tag.name'), primary_key=True)

class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(20), nullable=False)
  links = relationship('User_English_link', backref=backref('user', uselist=False))
  password = Column(Binary(128), nullable=False)

class English(Base):
  __tablename__ = 'English'
  id = Column(Integer, primary_key=True, autoincrement=True)
  links = relationship('User_English_link', backref=backref('English', uselist=False))
  word = Column(String(20), nullable=False)
  info = Column(Text)

class Tag(Base):
  __tablename__ = 'tag'
  name = Column(String(20), primary_key = True)
  links = relationship('User_English_link', backref=backref('tag', uselist=False))
