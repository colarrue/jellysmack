from fastapi.encoders import jsonable_encoder

import src.crud.base
import src.models


class Character(src.crud.base.BaseCrud):
    def __init__(self):
        super().__init__(src.models.Character)

    def filter_by_status(self, db, status, skip=0, limit=100):
        return db.query(self.model).filter(self.model.status == status).offset(skip).limit(limit).all()
