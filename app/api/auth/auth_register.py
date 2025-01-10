import sqlalchemy as sa
from fastapi import Response, Depends
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, model_validator  # Ganti dari root_validator ke model_validator
from werkzeug.security import generate_password_hash

from app.models.database import get_session
from app.models.database import User


class RegisterData(BaseModel):
    username: str
    full_name: str
    password: str
    confirm_password: str
    @model_validator(mode="before")  
    def validate_confirm_password(cls, values):
        password = values.get('password')
        confirm_password = values.get('confirm_password')
        if confirm_password != password:
            raise ValueError('Confirm password does not match')
        return values


async def auth_register(data: RegisterData, session = Depends(get_session)):
    check_username = session.execute(
        sa.select(
            User.id
        ).where(
            User.username == data.username
        )
    ).scalar()

    if check_username:
        raise HTTPException(400, detail='Username already used')
    encrypted_password = generate_password_hash(data.password)
    user = User(
        username=data.username,
        full_name=data.full_name,
        password=encrypted_password
    )
    session.add(user)
    session.commit()
    return Response(status_code=201)
