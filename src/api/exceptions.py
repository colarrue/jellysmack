import typing

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

import sqlalchemy.orm


class DatabaseException(Exception):
    def __init__(
        self,
        db: sqlalchemy.orm.Session,
        object_id: typing.Optional[int] = None,
        error_message: typing.Optional[str] = None,
    ):
        self.db_url = db.bind.url.database
        self.object_id = object_id
        self.error_message = error_message

    def not_found(self) -> str:
        return f"Object {self.object_id} not found in the database {self.db_url}"

    def integrity_error(self) -> str:
        return f"Integrity error {self.error_message} in the database {self.db_url}"


def database_exception_handler(request: Request, exception: DatabaseException) -> JSONResponse:
    if exception.error_message is not None:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT, content={"message": exception.integrity_error()}
        )
    elif exception.object_id is not None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": exception.not_found()}
        )
