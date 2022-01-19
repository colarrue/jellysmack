import typing

import sqlalchemy.orm

import src.crud.base
import src.models


class Character(src.crud.base.BaseCrud):
    def __init__(self):
        super().__init__(src.models.Character)

    def filter_by_status(
        self, db: sqlalchemy.orm.Session, status: str, skip: int = 0, limit: int = 100
    ) -> typing.List[src.models.Character]:
        return (
            db.query(self.model).filter(self.model.status == status).offset(skip).limit(limit).all()
        )
