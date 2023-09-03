from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    username: str
    email: EmailStr
    motto: str | None = None


class UserSchemaIn(UserBaseSchema):
    pass


class UserSchema(UserBaseSchema):
    id: int
