from enum import Enum
from typing import Optional

from pydantic import BaseModel

from app.models.schemas.utils import CustomDateTime, PageParam


class UserRoleEnum(int, Enum):
    reader = 10
    editor = 20
    admin = 40


class UserCreate(BaseModel):
    name: str
    email: str
    role: UserRoleEnum


class User(BaseModel):
    id: str
    name: str
    email: str
    role: UserRoleEnum
    created_at: CustomDateTime
    updated_at: CustomDateTime


class UserPatchPayload(BaseModel):
    role: UserRoleEnum


class UserGetParam(PageParam):
    name: Optional[str] = None
    email: Optional[str] = None


class Wink(BaseModel):
    last_login_at: Optional[CustomDateTime] = None
    role: UserRoleEnum
    realm: str
