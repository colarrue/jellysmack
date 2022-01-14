from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime

from src.db.database import Base

association_table = Table(
    "association",
    Base.metadata,
    Column("character_id", ForeignKey("character.id"), primary_key=True),
    Column("episode_id", ForeignKey("episode.id"), primary_key=True),
)


class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    status = Column(String)
    species = Column(String)
    type = Column(String)
    gender = Column(String)

    episodes = relationship("Episode", secondary=association_table, back_populates="characters")
    comments = relationship("Comment")


class Episode(Base):
    __tablename__ = "episode"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    air_date = Column(DateTime)
    episode = Column(String)

    characters = relationship("Character", secondary=association_table, back_populates="episodes")
    comments = relationship("Comment")


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    episode_id = Column(Integer, ForeignKey('episode.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
