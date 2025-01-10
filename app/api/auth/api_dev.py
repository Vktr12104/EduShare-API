import time
import sqlalchemy as sa
from pydantic import BaseModel
from fastapi import Depends
from fastapi.exceptions import HTTPException
from werkzeug.security import check_password_hash
from app.api_models.base_response import BaseResponseModel
from app.models.database import get_session
from app.config import config
from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
import uuid
from app.models.database import UserApi


def generate_api_key():
    return str(uuid.uuid4())

class APIKeyRequest(BaseModel):
    username: str

class PredictRequest(BaseModel):
    data: dict

async def request_api_key(request: APIKeyRequest, session = Depends(get_session)):
    username = request.username
    user = session.query(UserApi).filter(UserApi.username == username).first()
    if user:
        return {"api_key": user.api_key}
    new_api_key = generate_api_key()
    new_user = UserApi(username=username, api_key=new_api_key)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"api_key": new_user.api_key}




