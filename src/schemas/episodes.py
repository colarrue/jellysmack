import datetime
from typing import List, Optional
from pydantic import BaseModel

import src.schemas.characters


class Episode(BaseModel):
    id: int
    name: str
    air_date: datetime.datetime
    episode: str

    characters: List[src.schemas.characters.Character]

    class Config:
        orm_mode = True
