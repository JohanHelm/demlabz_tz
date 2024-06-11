from passlib.context import CryptContext

from app.db.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(user: User, password: str):
    if not user or not verify_password(password, user.pass_hash):
        return False
    return True
