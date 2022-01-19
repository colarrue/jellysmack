import typing

import src.db.database


# Dependency
def get_db() -> typing.Iterator:
    db = src.db.database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
