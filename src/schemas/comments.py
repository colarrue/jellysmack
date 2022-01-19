import typing

from pydantic import BaseModel


class Comment(BaseModel):
    id: typing.Optional[int]
    content: str
    episode_id: typing.Optional[int]
    character_id: typing.Optional[int]

    class Config:
        orm_mode = True
