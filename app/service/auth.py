import uuid
from fastapi import HTTPException , status
from app.schemas.schemas import UserRegister , UserResponse
from sqlalchemy.orm import Session
from app.service.security import hash_password, verify_password
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from app.db.models import User
def register_user(payload: UserRegister, db : Session):
    existing_user = db.scalar(
        select(User).where(
            (User.email==payload.email) |
            (User.username==payload.username)       
        )
    )
    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Username or email already exists"
        )
    user = User(
        user_id=uuid.uuid4(),
        username=payload.username,
        email=str(payload.email).lower(),
        pass_hash=hash_password(payload.password)
    )

    db.add(user)

    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Username or email already exists"
        )
    return {
        "user_id": str(user.user_id),
        "username": user.username,
        "email": user.email
    }