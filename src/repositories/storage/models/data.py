from datetime import UTC, datetime

from sqlalchemy import DateTime, Index, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Data(Base):
    __tablename__ = "data"

    ip: Mapped[str] = mapped_column(String(45), nullable=False)
    method: Mapped[str] = mapped_column(String(10), nullable=False)
    uri: Mapped[str] = mapped_column(String(2000), nullable=False)
    status_code: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
    )
    __table_args__ = (
        Index("idx_method_status", "method", "status_code"),
        Index("idx_data_created_at", "created_at"),
    )
