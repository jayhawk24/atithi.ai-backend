from enum import Enum


class TokenKind(Enum):
    RefreshToken = "refresh_token"
    AccessToken = "access_token"


class Roles(Enum):
    guest = "guest"
    host = "host"
    staff = "staff"
    admin = "admin"
