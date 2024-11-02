import uuid
from abc import ABC, abstractmethod
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.auth.core import Actor
from app.models.exceptions.base import CustomError
from app.models.schemas.source import (
    Author,
    AuthorCreate,
    Source,
    SourceAuthorAssociationCreate,
    SourceCreate,
)
from app.models.schemas.utils import PaginatedResponse
from app.models.sqlalchemy import (
    AuthorRecord,
    SourceAuthorAssociation,
    SourceRecord,
    UserRecord,
)
from app.repositories.util import translate_query_pagination
from app.models.schemas.utils import PaginatedResponse


class SqlAlchemySourceRepo:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_author(self, item_create: AuthorCreate, actor: Actor) -> Author:
        db_item = AuthorRecord(
            display_name=item_create.display_name,
            creator_id=actor.id,
        )
        self.db.add(db_item)
        self.db.flush()
        return Author.model_validate(db_item, from_attributes=True)

    def get_author(self, author_id: int) -> Author:
        db_item = self.db.query(AuthorRecord).get(author_id)
        if not db_item:
            raise CustomError(f"author id {author_id} not found")
        return Author.model_validate(db_item, from_attributes=True)
    

    def list_authors(self) -> PaginatedResponse[Author]:
        query = self.db.query(AuthorRecord)
        total = query.count()
        limit, offset, paging = translate_query_pagination(total=total)
        db_items = query.limit(limit).offset(offset)
        return PaginatedResponse[Author](
            data=[Author.model_validate(x, from_attributes=True) for x in db_items],
            paging=paging,
        )



    def create_source(self, item_create: SourceCreate, actor: Actor) -> Source:
        db_item = SourceRecord(
            display_name=item_create.display_name,
            publish_date=item_create.publish_date,
            pronounciation_category=item_create.pronounciation_category,
            creator_id=actor.id,
        )
        self.db.add(db_item)
        self.db.flush()
        return Source.model_validate(db_item, from_attributes=True)
    
    def get_source(self, source_id: int) -> Source:
        db_item = self.db.query(SourceRecord).get(source_id)
        if not db_item:
            raise CustomError(f"source id {source_id} not found")
        return Source.model_validate(db_item, from_attributes=True)
    
    def list_sources(self) -> PaginatedResponse[Source]:
        query = self.db.query(SourceRecord)
        total = query.count()
        limit, offset, paging = translate_query_pagination(total=total)
        db_items = query.limit(limit).offset(offset)
        return PaginatedResponse[Source](
            data=[Source.model_validate(x, from_attributes=True) for x in db_items],
            paging=paging,
        )
    
    def create_source_author_association(
        self, item_create: SourceAuthorAssociationCreate, actor: Actor
    ) -> SourceAuthorAssociation:
        db_item = SourceAuthorAssociation(
            author_id=item_create.author_id,
            source_id=item_create.source_id,
            role=item_create.role,
            age=item_create.age,
            creator_id=actor.id,
        )
        self.db.add(db_item)
        self.db.flush()
        return SourceAuthorAssociation.model_validate(db_item, from_attributes=True)
    
    def delete_source_author_association(self, association_id: int) -> None:
        db_item = self.db.query(SourceAuthorAssociation).get(association_id)
        if not db_item:
            raise CustomError(f"source author association id {association_id} not found")
        self.db.delete(db_item)
        self.db.flush()
