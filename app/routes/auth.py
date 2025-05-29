from fastapi import APIRouter, Depends
from app.schemas.auth import UserRegister, UserLogin, TokenResponse
from app.services.auth import register_user, login_user
from app.db.session import get_session
from sqlmodel import Session

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=TokenResponse)
def register(user: UserRegister, session: Session = Depends(get_session)):
    register_user(user, session)
    token = login_user(UserLogin(email=user.email, password=user.password), session)
    return token

@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin, session: Session = Depends(get_session)):
    return login_user(user, session)
