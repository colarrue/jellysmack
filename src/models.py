from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime


from src.db.database import Base


association_table = Table('association', Base.metadata,
    Column('characters_id', ForeignKey('characters.id'), primary_key=True),
    Column('episodes_id', ForeignKey('episodes.id'), primary_key=True)
)


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    status = Column(String)
    species = Column(String)
    type = Column(String)
    gender = Column(String)

    episodes = relationship("Episode", secondary=association_table, back_populates="characters")


class Episode(Base):
    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    air_date = Column(DateTime)
    episode = Column(String)

    characters = relationship("Character", secondary=association_table, back_populates="episodes")
