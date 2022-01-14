import datetime
from typing import List
from pydantic import BaseModel


class Episode(BaseModel):
    id: int
    name: str
    air_date: datetime.datetime
    episode: str

    characters: List

    class Config:
        orm_mode = True
