from datetime import datetime
from sqlalchemy import (
    Column,
    Enum,
    ForeignKey,
    String,
    Boolean,
    DateTime,
    Integer,
    JSON,
)
from commons.enums import Roles
from db.database import Base
from commons.utils import get_uuid
from sqlalchemy.ext.mutable import MutableList


class Rooms(Base):
    __tablename__ = "rooms"

    id = Column(String(50), primary_key=True, index=True, default=get_uuid)
    name = Column(String(50), nullable=False)
    images = Column(MutableList.as_mutable(JSON), nullable=True)
    no_of_beds = Column(Integer, nullable=True)
    occupancy = Column(Integer, nullable=True)

    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)


class UsersRooms(Base):
    __tablename__ = "users_rooms"

    id = Column(String(50), primary_key=True, index=True, default=get_uuid)
    user_id = Column(
        String(50), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    room_id = Column(
        String(50), ForeignKey("rooms.id", ondelete="CASCADE"), nullable=False
    )

    created_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)
