import sqlite3
import typing

from fastapi import APIRouter, Depends
import fastapi
import sqlalchemy.orm

import src.api.session
import src.api.exceptions
import src.crud.character
import src.models
import src.schemas.characters

router = APIRouter()


@router.get("/{character_id}", status_code=200, response_model=src.schemas.characters.Character)
def get_character(
    character_id: int, db: sqlalchemy.orm.Session = Depends(src.api.session.get_db)
) -> typing.Optional[src.models.Character]:
    character_crud = src.crud.character.Character()
    character = character_crud.get(db, character_id)
    if character is None:
        raise src.api.exceptions.DatabaseException(db, character_id)

    return character


@router.get("", status_code=200, response_model=typing.List[src.schemas.characters.Character])
def get_characters(
    offset: int = 0,
    limit: int = 10,
    status: str = None,
    db: sqlalchemy.orm.Session = Depends(src.api.session.get_db),
) -> typing.List[src.models.Character]:
    character_crud = src.crud.character.Character()

    if status is not None:
        characters = character_crud.filter_by_status(db, status, offset, limit)
    else:
        characters = character_crud.get_multi(db=db, skip=offset, limit=limit)

    return characters


@router.post("", status_code=201, response_model=src.schemas.characters.Character)
def create_character(
    character: src.schemas.characters.Character,
    db: sqlalchemy.orm.Session = Depends(src.api.session.get_db),
) -> src.models.Character:
    character_crud = src.crud.character.Character()
    try:
        character = character_crud.create(db, character)
    except sqlalchemy.exc.IntegrityError as err:
        raise src.api.exceptions.DatabaseException(db=db, error_message=err.args[0])
    return character
