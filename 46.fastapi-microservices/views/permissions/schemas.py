from pydantic import BaseModel


class CheckPermissionRequest(BaseModel):
    token: str
    action: str


class CheckPermissionResponse(BaseModel):
    allow: bool
    reason: str | None
