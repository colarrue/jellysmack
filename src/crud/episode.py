import src.crud.base
import src.models


class Episode(src.crud.base.BaseCrud):
    def __init__(self):
        super().__init__(src.models.Episode)
