from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.api.schemas.user import UserPersonalData, UserCreate
from app.dao.user_dao import get_user_dao, SqlAlchemyUserDAO
from app.db.models import User
from app.utils.user_jwt import create_access_token, get_user_from_token
from app.utils.user_pass import authenticate_user

user_router = APIRouter(
    prefix="/user",
    tags=["User"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login/")


@user_router.get("/")
async def get_root():
    return FileResponse("app/static/user_main.html")


@user_router.post("/new")
async def create_user(user_dao: SqlAlchemyUserDAO = Depends(get_user_dao),
                      form_data: OAuth2PasswordRequestForm = Depends()):
    pass


@user_router.post("/login")
async def login_for_access_token(user_dao: SqlAlchemyUserDAO = Depends(get_user_dao),
                                 form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    user: User = await user_dao.get_user(username)

    if not authenticate_user(user, password):
        raise HTTPException(status_code=401, detail="Invalid credentials", headers={"WWW-Authenticate": "Bearer"})

    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}


@user_router.get("/profile", response_model=UserPersonalData)
async def personal_data(user_dao: SqlAlchemyUserDAO = Depends(get_user_dao),
                        token: str = Depends(oauth2_scheme),
                        ):
    personal = get_user_from_token(token)
    username = personal.get("sub")

    user = await user_dao.get_user(username)
    user_personal_data = UserPersonalData(
        nickname=user.nickname,
        email=user.email,
        telegram_name=user.telegram_name,
        created_at=user.created_at,
        updated_at=user.updated_at
    )

    return user_personal_data
