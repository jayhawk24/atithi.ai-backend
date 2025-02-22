from datetime import datetime
from sqlalchemy import Column, Enum, String, Boolean, DateTime
from commons.enums import Roles
from db.database import Base
from commons.utils import get_uuid


class Users(Base):
    __tablename__ = "users"

    id = Column(String(50), primary_key=True, index=True, default=get_uuid)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, index=True)
    password = Column(String, nullable=False)
    role = Column(Enum(Roles), default=Roles.guest, nullable=False)
    avatar = Column(String, nullable=True)

    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)
