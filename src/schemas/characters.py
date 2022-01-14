from typing import Optional
from pydantic import BaseModel


class Character(BaseModel):
    id: int
    name: str
    status: str
    species: str
    type: Optional[str] = None
    gender: str

    class Config:
        orm_mode = True
