from fastapi import Depends, HTTPException
from app.dependencies.authentication import Authentication  
from pydantic import BaseModel
from sqlalchemy import select
import requests  
from fastapi import Depends, HTTPException
from app.dependencies.authentication import Authentication  
from app.models.database import Order
from app.models.database import User
from app.models.database import get_session
from pydantic import BaseModel
class OrderCreate(BaseModel):
    nama: str
    kuantitas: int
class EncryptRequest(BaseModel):
    text: str
    sensitivity: str

async def add_order(order_data: OrderCreate, user_id: int, session = Depends(get_session)):
    new_order = Order(
        user_id=user_id,
        nama=order_data.nama,
        kuantitas=order_data.kuantitas
    )
    session.add(new_order)
    session.commit()
    session.refresh(new_order)
    return new_order
async def create_order(order_data: OrderCreate, payload = Depends(Authentication()), session = Depends(get_session)):
    user_id = payload.get('uid', None)
    if user_id is None:
        raise HTTPException(status_code=401, detail="User not authorized")

    return await add_order(order_data, user_id=user_id, session=session)


async def get_prompt_encrypt(
    body: EncryptRequest,
    payload=Depends(Authentication())):
    FURINA_API_KEY="furina_32b8ad8042de4010ab9c9438bdee2ea7"
    user_id = payload.get("uid")
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authorized")
    encrypt_service_url = "https://furina-encryption-service.codebloop.my.id/api/encrypt"
    headers = {
        "accept": "application/json",
        "furina-encryption-service": FURINA_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": body.text,
        "sensitivity": body.sensitivity
    }
    try:
        # Melakukan permintaan POST ke API eksternal
        response = requests.post(
            encrypt_service_url,
            headers=headers,
            json=payload,
            timeout=10
        )
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error calling decryption service: {str(e)}"
        )
    
    # Parsing hasil respons
    encrypted_data  = response.json()

    # Mengembalikan hasil dekripsi
    return {
        "encrypt_cipher_recipe_result": encrypted_data
    }
