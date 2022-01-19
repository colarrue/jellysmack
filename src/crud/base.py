import abc
import typing

import fastapi.encoders
import pydantic
import sqlalchemy.orm


ModelType = typing.TypeVar("ModelType")
SchemaType = typing.TypeVar("SchemaType", bound=pydantic.BaseModel)


class BaseCrud(abc.ABC):
    def __init__(self, model: typing.Type[ModelType]):
        self.model = model

    def get(self, db: sqlalchemy.orm.Session, id: int) -> typing.Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(
        self, db: sqlalchemy.orm.Session, skip: int = 0, limit: int = 100
    ) -> typing.List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: sqlalchemy.orm.session.Session, obj_in: SchemaType) -> ModelType:
        obj_in_data = fastapi.encoders.jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj  # type: ignore

    def update(
        self, db: sqlalchemy.orm.Session, db_obj: ModelType, obj_in: SchemaType
    ) -> ModelType:
        obj_data = fastapi.encoders.jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: sqlalchemy.orm.Session, id: int) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj  # type: ignore
