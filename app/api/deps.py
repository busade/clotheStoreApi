from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    """TODO: Decode bearer JWT, validate subject, and fetch the active user."""
    # TODO 1: Decode token and require a valid subject claim.
    # TODO 2: Fetch the user; return 401 for invalid, missing, or inactive accounts.
    raise HTTPException(status_code=501, detail="Not implemented")

def get_current_admin(current_user: User = Depends(get_current_user)) -> User:
    """TODO: Permit administrators only; return 403 for customers."""
    # TODO 1: Compare current_user.role to the admin role.
    raise HTTPException(status_code=501, detail="Not implemented")
