from pydantic import BaseModel, EmailStr, validator


class UserBase(BaseModel):
    """Shared props received via API on update"""

    firstname: str | None
    lastname: str | None
    email: EmailStr
    phone_number: str | None
    address: str | None
    gender: int | None


class UserCreate(UserBase):
    """Props received via API on create"""

    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "mail@example.com",
                "password": "strong1password",
                "gender": 1,
            }
        }


class UserUpdate:
    """Props received via API on update"""

    firstname: str | None
    lastname: str | None
    email: EmailStr | None
    phone_number: str | None
    address: str | None
    gender: int | None
    password: str | None


class UserInDBBase(UserBase):
    id: int | None
    is_admin: bool
    is_staff: bool

    class Config:
        orm_mode = True


class User(UserInDBBase):
    """Properties to return via API"""

    pass


class UserInDB(UserInDBBase):
    """Properties stored in DB"""

    hashed_password: str
