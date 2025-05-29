from sqlmodel import Session, select
from app.models.user import User
from app.schemas.auth import UserRegister, UserLogin
from app.core.security import hash_password, verify_password, create_access_token
from app.db.session import get_session
from fastapi import HTTPException, Depends

def register_user(user_data: UserRegister, session: Session):
    existing_user = session.exec(select(User).where(User.email == user_data.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email ya registrado")

    user = User(
        name=user_data.name,
        lastname=user_data.lastname,
        email=user_data.email,
        password=hash_password(user_data.password)
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def login_user(data: UserLogin, session: Session):
    user = session.exec(select(User).where(User.email == data.email)).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
