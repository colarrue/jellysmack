from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime

from src.db.database import Base


class Episode(Base):
    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    air_date = Column(DateTime)
    episode = Column(String)
