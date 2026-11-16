def test_register_success(client):
    response = client.post("/api/v1/auth/register", json={"email": "new@test.com", "password": "Password123!", "full_name": "New User"})
    assert response.status_code == 201
    assert response.json()["email"] == "new@test.com"

def test_register_duplicate_email(client):
    payload = {"email": "same@test.com", "password": "Password123!", "full_name": "Same"}
    assert client.post("/api/v1/auth/register", json=payload).status_code == 201
    assert client.post("/api/v1/auth/register", json=payload).status_code == 400

def test_login_success(client, db, customer):
    response = client.post("/api/v1/auth/login", data={"username": customer.email, "password": "Password123!"})
    assert response.status_code == 200 and response.json()["token_type"] == "bearer"

def test_login_wrong_password(client, customer):
    assert client.post("/api/v1/auth/login", data={"username": customer.email, "password": "wrong"}).status_code == 401

def test_me_authenticated_and_unauthenticated(client):
    assert client.get("/api/v1/auth/me").status_code == 200
    from app.api.deps import get_current_user
    identity = client.app.dependency_overrides.pop(get_current_user)
    try:
        assert client.get("/api/v1/auth/me").status_code == 401
    finally:
        client.app.dependency_overrides[get_current_user] = identity
