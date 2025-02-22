from rooms.models import Rooms, UsersRooms
from rooms.schemas import RoomSchema
from users.models import Users
from fastapi import Depends, HTTPException, status, APIRouter

from sqlalchemy.orm import Session
from db.database import get_db
from auth.tokens import get_current_user

rooms_router = APIRouter(prefix="/rooms", tags=["Rooms"])


@rooms_router.get("/")
async def get_rooms(
    user: Users = Depends(get_current_user), db: Session = Depends(get_db)
) -> RoomSchema:
    rooms = db.query(Rooms).join(UsersRooms).filter(UsersRooms.user_id == user.id).all()

    return rooms
