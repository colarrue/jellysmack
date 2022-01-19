from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import typing

import src.api.session
import src.crud.comment
import src.models
import src.schemas.comments

router = APIRouter()


@router.get("/{comment_id}", status_code=200, response_model=src.schemas.comments.Comment)
def get_comment(
    comment_id: int, db: Session = Depends(src.api.session.get_db)
) -> typing.Optional[src.models.Comment]:
    comment_crud = src.crud.comment.Comment()
    return comment_crud.get(db, comment_id)


@router.get("", status_code=200, response_model=typing.List[src.schemas.comments.Comment])
def get_comments(
    offset: int = 0, limit: int = 10, db: Session = Depends(src.api.session.get_db)
) -> typing.List[src.models.Comment]:
    comment_crud = src.crud.comment.Comment()
    return comment_crud.get_multi(db=db, skip=offset, limit=limit)


@router.post("", status_code=201, response_model=src.schemas.comments.Comment)
def create_comment(
    comment: src.schemas.comments.Comment, db: Session = Depends(src.api.session.get_db)
) -> src.models.Comment:
    character_crud = src.crud.comment.Comment()
    return character_crud.create(db, comment)


@router.delete("/{comment_id}", status_code=204)
def delete_comment(comment_id, db: Session = Depends(src.api.session.get_db)) -> None:
    comment_crud = src.crud.comment.Comment()
    comment_crud.remove(db, comment_id)
