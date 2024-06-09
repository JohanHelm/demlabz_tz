from fastapi import APIRouter


user_router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@user_router.get("/")
async def get_user():
    pass


@user_router.post("/")
async def create_user():
    pass
