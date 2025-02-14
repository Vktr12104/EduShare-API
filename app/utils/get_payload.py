import jwt

from app.config import config


def get_payload(access_token: str, verify_exp: bool = True) -> dict:
    payload = jwt.decode(access_token, config.PUBLIC_KEY, ['RS256'], options={'verify_exp': verify_exp})

    return payload