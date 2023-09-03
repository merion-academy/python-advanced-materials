from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    username: str
    email: EmailStr
    motto: str | None = None


class UserCreateSchema(UserBaseSchema):
    pass


class UserUpdateSchema(UserBaseSchema):
    username: str | None = None
    email: EmailStr | None = None
    motto: str | None = None


class UserSchema(UserBaseSchema):
    id: int
