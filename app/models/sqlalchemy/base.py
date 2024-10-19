from sqlalchemy.orm import declarative_base
from datetime import datetime

from sqlalchemy import DateTime, BIGINT
from sqlalchemy.orm import Mapped, mapped_column

Base = declarative_base()


class AdminRecord(Base):
    creator_id: Mapped[int] = mapped_column(BIGINT, nullable=False)
    create_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updater_id: Mapped[int] = mapped_column(BIGINT, nullable=True)
    update_time: Mapped[datetime] = mapped_column(DateTime, nullable=True)