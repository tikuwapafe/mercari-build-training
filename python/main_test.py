from fastapi.testclient import TestClient
from .main import app, get_db
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from python import models

# Create the SQLAlchemy base and engine
engine = create_engine('sqlite:///python/db/test_mercari.sqlite3', connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def db_connection():
    db = SessionLocal() 
    # Before the test is done, create a test database
    models.Base.metadata.create_all(bind=engine)
    yield db 
    db.close()
    # After the test is done, remove the test database
    models.Base.metadata.drop_all(bind=engine) 

client = TestClient(app)


@pytest.mark.parametrize(
    "want_status_code, want_body",
    [
        (200, {"message": "Hello, world!"}),
    ],
)
def test_hello(want_status_code, want_body):
    response = client.get("/")
    assert response.status_code == want_status_code #confirm the status code
    assert response.json() == want_body #confirm response body


@pytest.mark.parametrize(
    "args, want_status_code",
    [
        ({"name":"used iPhone 16e", "category":"phone"}, 200),
        ({"name":"", "category":"phone"}, 400),
    ],
)
def test_add_item_e2e(args, want_status_code, db_connection: Session):
    response = client.post("/items/", data=args)
    assert response.status_code == want_status_code

    if want_status_code >= 400:
        return  
    
    # Check if the response body is correct
    response_data = response.json()
    assert "message" in response_data

    # Check if the data was saved to the database correctly
    db_item = db_connection.query(models.Items).\
                            filter(models.Items.name == args["name"]).one_or_none()
    assert db_item is not None
    assert db_item.name == args["name"]
