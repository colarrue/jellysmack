import abc
from fastapi.encoders import jsonable_encoder


class BaseCrud(abc.ABC):
    def __init__(self, model):
        self.model = model

    def get(self, db, id):
        return db.query(self.model).filter(self.model.id == id).first()

    def create(self, db, obj_in):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db, db_obj, obj_in):
        obj_data = jsonable_encoder(db_obj)
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

    def remove(self, db, id):
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
