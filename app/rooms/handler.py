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


@rooms_router.get("/room-code/{room_code}")
async def get_room_by_code(
    room_code: str,
    db: Session = Depends(get_db),
) -> RoomSchema:
    room = db.query(Rooms).filter(Rooms.code == room_code).first()

    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Room not found",
        )

    return room


@rooms_router.get("/{room_id}")
async def get_room(
    room_id: str, user: Users = Depends(get_current_user), db: Session = Depends(get_db)
) -> RoomSchema:
    room = db.query(Rooms).filter(Rooms.id == room_id).first()

    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Room not found",
        )

    return room
