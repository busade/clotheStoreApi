import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.db.base import Base
from app.db.base import Base
from app.db.session import get_db
from app.api.deps import get_current_user, get_current_admin
from app.main import app
from app.models import Product, ProductCategory, ProductSize, User, UserRole
from app.core.security import hash_password

@pytest.fixture()
def db():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    testing_session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    Base.metadata.create_all(engine)
    session = testing_session()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(engine)
        engine.dispose()

@pytest.fixture()
def customer(db):
    user = User(email="customer@test.com", hashed_password=hash_password("Password123!"), full_name="Test Customer", role=UserRole.customer)
    db.add(user); db.commit(); db.refresh(user)
    return user

@pytest.fixture()
def admin(db):
    user = User(email="admin@test.com", hashed_password=hash_password("Password123!"), full_name="Test Admin", role=UserRole.admin)
    db.add(user); db.commit(); db.refresh(user)
    return user

@pytest.fixture()
def sample_product(db):
    item = Product(name="Test Tee", description="A tee", price="20.00", category=ProductCategory.Shirts, size=ProductSize.M, color="Black", stock_quantity=5)
    db.add(item); db.commit(); db.refresh(item)
    return item

@pytest.fixture()
def client(db, customer, admin):
    def override_get_db():
        yield db
    app.dependency_overrides[get_db] = override_get_db
    # Once auth is implemented, replace these test identity overrides with JWT headers
    # for tests that specifically exercise authentication and role checks.
    app.dependency_overrides[get_current_user] = lambda: customer
    app.dependency_overrides[get_current_admin] = lambda: admin
    yield TestClient(app)
    app.dependency_overrides.clear()

@pytest.fixture()
def customer_client(db, customer):
    def override_get_db():
        yield db
    def deny_admin():
        raise HTTPException(status_code=403, detail="Forbidden")
    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_current_user] = lambda: customer
    app.dependency_overrides[get_current_admin] = deny_admin
    yield TestClient(app)
    app.dependency_overrides.clear()

@pytest.fixture()
def admin_client(db, admin):
    def override_get_db():
        yield db
    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[get_current_user] = lambda: admin
    app.dependency_overrides[get_current_admin] = lambda: admin
    yield TestClient(app)
    app.dependency_overrides.clear()
