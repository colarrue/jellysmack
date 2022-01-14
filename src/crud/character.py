from fastapi.encoders import jsonable_encoder

import src.crud.base
import src.models


class Character(src.crud.base.BaseCrud):
    def __init__(self):
        super().__init__(src.models.Character)
