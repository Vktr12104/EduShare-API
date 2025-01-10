import time
import sqlalchemy as sa
from pydantic import BaseModel
from fastapi import Depends
from fastapi.exceptions import HTTPException
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta

from app.api_models.base_response import BaseResponseModel
from app.models.database import User
from app.models.database import UserLogin
from app.models.database import get_session
from app.config import config
from app.utils.generate_refresh_token import generate_refresh_token
from app.utils.generate_access_token import generate_access_token


class LoginData(BaseModel):
    username: str
    password: str


class LoginDataResponseModel(BaseModel):
    user_id: int
    refresh_token: str
    access_token: str
    expired_at: int


class LoginResponseModel(BaseResponseModel):
    data: LoginDataResponseModel

    class Config:
        schema_extra = {
            'example': {
                'data': {
                    'user_id': 1000,
                    'refresh_token': 'abc.def.ghi',
                    'acces_token': 'jkl.mno.pqr',
                    'expired_at': 123456
                },
                'meta': {},
                'message': 'Success',
                'success': True,
                'code': 200
            }
        }


async def auth_login(data: LoginData, session = Depends(get_session)):
    # Periksa username
    user = session.execute(
        sa.select(
            User.id,
            User.password
        ).where(
            User.username == data.username
        )
    ).fetchone()

    if not user or not check_password_hash(user.password, data.password):
        raise HTTPException(400, detail='Username/password does not match')

    payload = {
        'uid': user.id,
        'username': data.username
    }

    # Generate refresh token
    refresh_token = generate_refresh_token(payload)

    # Hitung expired_at menggunakan Python
    refresh_token_expiration_seconds = config.REFRESH_TOKEN_EXPIRATION
    expired_at = datetime.utcnow() + timedelta(seconds=refresh_token_expiration_seconds)

    # Buat objek UserLogin
    user_login = UserLogin(
        user_id=user.id,
        refresh_token=refresh_token,
        expired_at=expired_at,
        created_at=datetime.utcnow(),
        modified_at=datetime.utcnow()
    )

    session.add(user_login)
    session.commit()

    # Generate access token
    access_token, access_token_expired_at = generate_access_token(payload)

    return LoginResponseModel(
        data=LoginDataResponseModel(
            user_id=user.id,
            refresh_token=refresh_token,
            access_token=access_token,
            expired_at=access_token_expired_at
        )
    )