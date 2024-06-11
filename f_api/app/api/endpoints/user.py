import datetime
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.user import UserPersonalData, UserCreate, UserUpdate
from app.dao.user_dao import UserDAO
from app.db.db_settings import get_async_session
from app.db.models import User
from app.utils.user_jwt import create_access_token, get_user_from_token
from app.utils.user_pass import authenticate_user, get_password_hash

user_router = APIRouter(
    prefix="/user",
    tags=["User"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login/")


async def get_user_dao(session: AsyncSession = Depends(get_async_session)) -> UserDAO:
    return UserDAO(session)


@user_router.get("/")
async def get_root():
    return FileResponse("app/static/user_main.html")


@user_router.post("/new")
async def create_user(user_data: UserCreate,
                      user_dao: UserDAO = Depends(get_user_dao)):

    await user_dao.add_one({"nickname": user_data.nickname,
                            "pass_hash": get_password_hash(user_data.open_pass),
                            "email": user_data.email,
                            "telegram_name": user_data.telegram_name})
    return user_data


@user_router.post("/login")
async def login_for_access_token(user_dao: UserDAO = Depends(get_user_dao),
                                 form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    user: User = await user_dao.get_one(username)

    if not authenticate_user(user, password):
        raise HTTPException(status_code=401, detail="Invalid credentials", headers={"WWW-Authenticate": "Bearer"})

    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}


@user_router.get("/profile", response_model=UserPersonalData)
async def personal_data(user_dao: UserDAO = Depends(get_user_dao),
                        token: str = Depends(oauth2_scheme)
                        ):
    personal = get_user_from_token(token)
    username = personal.get("sub")

    user = await user_dao.get_one(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_personal_data = UserPersonalData.model_validate(user)
    return user_personal_data


@user_router.put("/edit", response_model=UserUpdate)
async def update_user_data(edit_user_data: UserUpdate,
                           user_dao: UserDAO = Depends(get_user_dao),
                           token: str = Depends(oauth2_scheme)
                           ):
    personal = get_user_from_token(token)
    username = personal.get("sub")
    user = await user_dao.get_one(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = edit_user_data.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.datetime.now()
    for key, value in update_data.items():
        setattr(user, key, value)

    await user_dao.update_one(user)
    return edit_user_data
