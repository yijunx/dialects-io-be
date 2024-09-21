from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.sqlalchemy.base import Base

# these tables are inspired by prisma schema


class UserORM(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    role: Mapped[str] = mapped_column(String, nullable=False)
    realm: Mapped[str] = mapped_column(String, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    last_login_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class StandardCharacterORM(Base):
    __tablename__ = "standard_characters"
    id: Mapped[str] = mapped_column(String, primary_key=True)

    # 標準字形
    standard_form: Mapped[str] = mapped_column(String, nullable=False, index=True)

    common_form_id: Mapped[str] = mapped_column(
        String, ForeignKey("common_characters.id"), nullable=False
    )

    # 意思
    meaning: Mapped[str] = mapped_column(String, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class CommonCharacterORM(Base):
    __tablename__ = "common_characters"
    id: Mapped[str] = mapped_column(String, primary_key=True)

    # 常用字形
    common_form: Mapped[str] = mapped_column(String, nullable=False, index=True)

    # 由来
    meaning: Mapped[str] = mapped_column(String, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class WordORM(Base):
    __tablename__ = "words"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    # 標準字形
    standard_form: Mapped[str] = mapped_column(String, nullable=False, index=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class PronounciationORM(Base):
    __tablename__ = "pronounciations"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    charactor_id: Mapped[str] = mapped_column(String, nullable=False)

    # 標準音，吳語拼音
    wu_repr: Mapped[str] = mapped_column(String, nullable=False)
    # 標準音，廣韻
    canton_repr: Mapped[str] = mapped_column(String, nullable=False)
    # 標準音，國際音標
    phonetic_repr: Mapped[str] = mapped_column(String, nullable=False)

    # 描述
    description: Mapped[str] = mapped_column(String, nullable=True)

    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)


class SourceORM(Base):
    __tablename__ = "sources"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
