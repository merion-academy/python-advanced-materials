from pydantic import BaseModel


class MulRequest(BaseModel):
    a: int
    b: int
