from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict


class RoomSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    images: List[str] = None
    no_of_beds: int
    occupancy: int
    is_active: bool
    created_at: datetime
    updated_at: datetime
