from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate

def register_user(payload: UserCreate, db: Session):
    """TODO: Register a customer and return its public profile."""
    # TODO 1: Reject an email already in use with 400.
    # TODO 2: Hash the password; never persist the submitted password.
    # TODO 3: Create a customer User, commit, refresh, and return it (201).
    raise HTTPException(status_code=501, detail="Not implemented")

def login_user(username: str, password: str, db: Session):
    """TODO: Verify credentials and return a signed bearer token."""
    # TODO 1: Look up email and verify its hash; use 401 when credentials fail.
    # TODO 2: Create JWT claims containing sub=user id and role.
    # TODO 3: Return Token(access_token=..., token_type="bearer").
    raise HTTPException(status_code=501, detail="Not implemented")

def get_user_profile(current_user):
    """TODO: Return the authenticated user's safe profile."""
    # TODO 1: Return current_user; response schema excludes password hash.
    raise HTTPException(status_code=501, detail="Not implemented")
