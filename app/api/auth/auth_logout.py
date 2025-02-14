import sqlalchemy as sa
from fastapi import Depends, Response
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

from app.models.database import UserLogin
from app.models.database import get_session


class LogoutData(BaseModel):
    refresh_token: str


async def auth_logout(data: LogoutData, session = Depends(get_session)):
    result = session.execute(
        sa.delete(UserLogin).where(UserLogin.refresh_token == data.refresh_token)
    )

    if result.rowcount == 0:
        raise HTTPException(400, 'Refresh token not found')
    
    session.commit()

    return Response(status_code=204)