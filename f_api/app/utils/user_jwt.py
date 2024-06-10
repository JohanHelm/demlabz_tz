from fastapi import HTTPException
from datetime import datetime, timedelta
import jwt

from app.core.config import Settings

jwt_settings = Settings().jwt_settigs_dict()

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=jwt_settings["expire"])
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, jwt_settings["secret_key"], algorithm=jwt_settings["algoritm"])
    return encoded_jwt


def get_user_from_token(token: str):
    try:
        payload = jwt.decode(token, jwt_settings["secret_key"], algorithms=[jwt_settings["algoritm"]])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired", headers={"WWW-Authenticate": "Bearer"})
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Invalid token", headers={"WWW-Authenticate": "Bearer"})
