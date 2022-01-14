import src.db.database


# Dependency
def get_db():
    db = src.db.database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
