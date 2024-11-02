from datetime import date, datetime

from sqlalchemy import ARRAY, BIGINT, DATE, VARCHAR, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.sqlalchemy.base import AdminRecord, Base


class AuthorRecord(AdminRecord):
    __tablename__ = "author"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    # 鮑仕傑
    display_name: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)


class SourceRecord(AdminRecord):
    __tablename__ = "source"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    # 杭語詞典（我們自己的詞典）
    display_name: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    publish_date: Mapped[date] = mapped_column(DATE, nullable=True)
    pronounciation_category: Mapped[list] = mapped_column(
        ARRAY(VARCHAR(50)), nullable=True
    )


class SourceAuthorAssociation(AdminRecord):
    __tablename__ = "source_author_association"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    author_id: Mapped[int] = mapped_column(BIGINT, nullable=False, index=True)
    source_id: Mapped[int] = mapped_column(BIGINT, nullable=False, index=True)

    # author or pronouncer
    role: Mapped[str] = mapped_column(VARCHAR(50), nullable=True)
    # mainly for pronouncer, well, we can also use it for author, haha
    age: Mapped[int] = mapped_column(Integer, nullable=True)
