from pydantic import BaseModel


class Comment(BaseModel):
    id: int = None
    content: str
    episode_id: int = None
    character_id: int = None

    class Config:
        orm_mode = True
