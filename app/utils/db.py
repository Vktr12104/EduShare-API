import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import config
db_engine = sa.create_engine(
    config.DB,
    pool_pre_ping=config.DB_POOL_PRE_PING,
    pool_size=config.DB_POOL_SIZE,
    pool_recycle=config.DB_POOL_RECYCLE,
    echo=config.DB_ECHO
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
Base = declarative_base()
