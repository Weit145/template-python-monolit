from datetime import UTC, datetime

from sqlalchemy import DateTime, Index
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Stats(Base):
    __tablename__ = "stats"

    methods: Mapped[dict[str, int]] = mapped_column(JSONB, nullable=False)
    status_codes: Mapped[dict[str, int]] = mapped_column(JSONB, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
    )
    __table_args__ = (Index("idx_created_at", "created_at"),)
