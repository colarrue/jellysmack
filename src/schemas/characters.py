from typing import List, Optional
from pydantic import BaseModel

import src.schemas.episodes


class Character(BaseModel):
    id: int
    name: str
    status: str
    species: str
    type: Optional[str] = None
    gender: str

    episodes = List[src.schemas.episodes.Episode]

    class Config:
        orm_mode = True
