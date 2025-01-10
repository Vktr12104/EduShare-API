import time
import jwt
from dotenv import load_dotenv
import os

load_dotenv()

def generate_refresh_token(payload: dict) -> str:
    current_time = int(time.time())

    payload.update({
        'iat': current_time
    })
    refresh_token = jwt.encode(payload, os.getenv('REFRESH_PRIVATE_KEY').encode('utf-8'), 'RS256')

    return refresh_token
