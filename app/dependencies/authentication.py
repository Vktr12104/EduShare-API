from typing import Optional
import jwt
from fastapi import Request, Depends
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from fastapi.exceptions import HTTPException
from fastapi.security import APIKeyHeader
from app.models.database import get_session
from app.models.database import UserApi
from app.utils.get_payload import get_payload

API_KEY_HEADER = APIKeyHeader(name="Authentication")
class Authentication(HTTPBearer):
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        authorization = await super().__call__(request)

        try:
            payload = get_payload(authorization.credentials)
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                401,
                detail={
                    'message': 'Token expired',
                    'code': 40100
                }
            )
        except jwt.DecodeError:
            raise HTTPException(
                401,
                detail={
                    'message': 'Token invalid',
                    'code': 40101
                }
            )
        
        return payload


async def verify_api_key(
    api_key: str = Depends(API_KEY_HEADER), 
    session=Depends(get_session)
):
    # Query untuk memeriksa UserApi dengan API key tertentu
    user = session.exec(
        UserApi.select().where(UserApi.api_key == api_key)
    ).first()

    if not user:
        raise HTTPException(
            status_code=403, 
            detail="Invalid API key"
        )
    return user