from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr

class UserLogin(UserBase):
    password: str

class UserRegister(UserBase):
    name: str
    hashed_password: str

class UserToken(UserBase):
    token: str
