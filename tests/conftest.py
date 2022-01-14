import pytest

import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.db.database import Base
from src.main import app
from src.api.session import get_db
import scripts.init_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

scripts.init_db.init_database(
    os.path.abspath("./test.db"),
    TestingSessionLocal(),
    "test_characters.json",
    "test_episodes.json",
)


@pytest.fixture()
def client():
    return TestClient(app)
