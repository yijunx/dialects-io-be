from datetime import datetime

from sqlalchemy import DateTime, UUID, String
from sqlalchemy.orm import Mapped, mapped_column
import uuid
from app.models.sqlalchemy.base import Base


class UserRecord(Base):
    __tablename__ = "user"

    # cos keycloak uses uuid...
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)

    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    nick_name: Mapped[str] = mapped_column(String, nullable=True)

    role: Mapped[str] = mapped_column(String, nullable=False)
    realm: Mapped[str] = mapped_column(String, nullable=True)

    create_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    update_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    last_login_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
