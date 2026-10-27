from fastapi import APIRouter, Depends, status
from app.schemas.schemas import UserRegister , UserResponse
from app.service.auth import register_user
from sqlalchemy.orm import Session
from app.db.database import get_db
from sqlalchemy import select
from app.db.models import User
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def reg_usr(payload: UserRegister, db:Session = Depends(get_db)):
    return register_user(payload,db)
