from datetime import date
from typing import Optional

from pydantic import BaseModel


class AuthorCreate(BaseModel):
    display_name: str


class Author(AuthorCreate):
    id: int


class SourceCreate(BaseModel):
    display_name: str
    publish_date: date
    pronounciation_category: list[str]


class Source(SourceCreate):
    id: int


class SourceAuthorAssociationCreate(BaseModel):
    author_id: int
    source_id: int
    role: str
    age: Optional[int] = None
