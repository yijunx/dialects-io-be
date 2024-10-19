from datetime import datetime, date

from sqlalchemy import JSON, DateTime, Index, BIGINT, VARCHAR, DATE, Integer, ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from app.models.sqlalchemy.base import Base



class AuthorRecord(Base):
    __tablename__ = "author"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    # 鮑仕傑
    display_name: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)

    # admin fields
    creator_id: Mapped[int] = mapped_column(BIGINT, nullable=False)
    create_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updater_id: Mapped[int] = mapped_column(BIGINT, nullable=True)
    update_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class SourceRecord(Base):
    __tablename__ = "source"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    # 杭語詞典（我們自己的詞典）
    display_name: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    publish_date: Mapped[datetime] = mapped_column(DATE, nullable=True)
    pronounciation_category: Mapped[list] = mapped_column(ARRAY(VARCHAR(50)), nullable=True)

    # admin fields
    creator_id: Mapped[int] = mapped_column(BIGINT, nullable=False)
    create_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updater_id: Mapped[int] = mapped_column(BIGINT, nullable=True)
    update_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class SourceAuthorAssociation(Base):
    __tablename__ = "source_author_association"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    author_id: Mapped[int] = mapped_column(BIGINT, nullable=False, index=True)
    source_id: Mapped[int] = mapped_column(BIGINT, nullable=False, index=True)

    # author or pronouncer
    contribution_as_what: Mapped[str] = mapped_column(VARCHAR(50), nullable=True)
    # mainly for pronouncer
    contribution_as_age: Mapped[int] = mapped_column(Integer, nullable=True)

    # admin fields
    creator_id: Mapped[int] = mapped_column(BIGINT, nullable=False)
    create_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updater_id: Mapped[int] = mapped_column(BIGINT, nullable=True)
    update_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
