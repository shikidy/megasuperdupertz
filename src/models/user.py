from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class UserModel(Base):
    """User model
    """
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    """Telegrams id"""
    username: Mapped[Optional[str]] = mapped_column(nullable=True)
    """Telegram username. May be None."""
    firstname: Mapped[str] = mapped_column(nullable=False)
    """Telegram firstame"""
