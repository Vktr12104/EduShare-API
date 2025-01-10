
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String

from app.models import Base

class UserApi(Base):
    __tablename__ = "users_api"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    api_key = Column(String, unique=True, nullable=False)