from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import typing

import src.api.session
import src.crud.episode
import src.models
import src.schemas.episodes

router = APIRouter()


@router.get("/{episode_id}", status_code=200, response_model=src.schemas.episodes.Episode)
def get_episode(
    episode_id: int, db: Session = Depends(src.api.session.get_db)
) -> typing.Optional[src.models.Episode]:
    episode_crud = src.crud.episode.Episode()
    return episode_crud.get(db, episode_id)


@router.get("", status_code=200, response_model=typing.List[src.schemas.episodes.Episode])
def get_episodes(
    max_results: int, db: Session = Depends(src.api.session.get_db)
) -> typing.List[src.models.Episode]:
    episode_crud = src.crud.episode.Episode()
    return episode_crud.get_multi(db=db, limit=max_results)
