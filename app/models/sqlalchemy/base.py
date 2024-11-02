import uuid
from datetime import datetime, timezone

from sqlalchemy import UUID, DateTime
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base = declarative_base()


class AdminRecord(Base):
    creator_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    create_time: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    updater_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=True)
    update_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)
