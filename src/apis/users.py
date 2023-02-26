from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/", tags=["users"])
async def read_users():
    return [{"username": "huong"}, {"username": "oanh"}]


@router.get("/me", tags=["users"])
async def read_user_me():
    return {"username": "huongpx"}


@router.get("/{username}", tags=["users"])
async def read_user(username: str, age: int = 25):
    return {"username": username}
