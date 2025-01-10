from fastapi import FastAPI, HTTPException
from app.models.database import get_session
from app.models.database import Collections
from fastapi import Depends

async def get_all_collections(sort_by: str = None, session = Depends(get_session)):
    collections = session.query(Collections).all()

    if sort_by:
        if hasattr(Collections, sort_by):
            collections = session.query(Collections).order_by(getattr(Collections, sort_by)).all()
        else:
            raise HTTPException(status_code=400, detail=f"Invalid sort key: {sort_by}")

    return collections

async def get_collection_by_id(collect_id: int,session = Depends(get_session)):
    collection = session.query(Collections).filter(Collections.id == collect_id).first()
    if not collection:
        raise HTTPException(status_code=404, detail="Item not found!")
    
    return collection

