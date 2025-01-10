from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, create_engine, Session
from app.config import config

import logging

# Logging untuk debugging
logging.basicConfig(level=logging.INFO)
sqlite_file_name = "database.db"
sqlite_url = "sqlite:///database.db"
connect_args = {"check_same_thread": False}


# Menggunakan URL database dari konfigurasi
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)
class Collections(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nama: str = Field(index=True)
    kategori: str = Field(index=True)
    harga: str
    durasi: Optional[int] = Field(default=None)
    diskon: Optional[int] = Field(default=None)
    jarak: Optional[int] = Field(default=None)

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, index=True)
    nama: str
    kuantitas: Optional[int] = Field(default=None)
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    full_name: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(default_factory=datetime.now)

class UserApi(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    api_key: str = Field(unique=True)

class UserLogin(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, index=True)
    refresh_token: str
    expired_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(default_factory=datetime.now)



# Membuat tabel dari model SQLModel
def create_tables():
    logging.info("Creating tables in the database...")
    SQLModel.metadata.create_all(engine)
    logging.info("Tables created successfully!")

# Membuka session untuk operasi database
def get_session():
    with Session(engine) as session:
        yield session
