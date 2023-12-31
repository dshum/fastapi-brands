from fastapi import APIRouter

from lib.user import fastapi_users, auth_backend
from schemas.users import UserRead, UserUpdate, UserCreate

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt"
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)

router.include_router(
    fastapi_users.get_reset_password_router(),
)

router.include_router(
    fastapi_users.get_verify_router(UserRead),
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
)
