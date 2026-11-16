from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.api.deps import get_current_user
from app.schemas.user import UserCreate, UserRead
from app.schemas.token import Token
from app.controllers import auth_controller as ctl

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    return ctl.register_user(payload, db)

@router.post("/login", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return ctl.login_user(form.username, form.password, db)

@router.get("/me", response_model=UserRead)
def me(current_user=Depends(get_current_user)):
    return ctl.get_user_profile(current_user)
