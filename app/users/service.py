from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import get_password_hash

from .schemas import RegisterForm, UserUpdate
from .models import User
from .repository import UserRepository


async def create_user(session: AsyncSession, user_data: RegisterForm) -> User:
    if await UserRepository.get_user_by_email(session, str(user_data.email)):
        raise HTTPException(409, "Email уже зарегистрирован в системе")
    if await UserRepository.get_user_by_username(session, user_data.username):
        raise HTTPException(409, "Имя пользователя уже занято")
    if len(user_data.password) < 8:
        raise HTTPException(400, "Пароль должен содержать минимум 8 символов")

    user = User(
        email=str(user_data.email),
        hashed_password=get_password_hash(user_data.password),
        username=user_data.username,
        full_name=user_data.full_name,
    )

    return await UserRepository.create_user(session, user)


async def update_user_service(session: AsyncSession, user_id: int, user_data: UserUpdate) -> User | None:
    user = await UserRepository.get_user_by_id(session, user_id)

    if not user:
        raise HTTPException(404, "Пользователь не найден")

    user_data = user_data.model_dump(exclude_unset=True)

    if "password" in user_data:
        user_data["hashed_password"] = get_password_hash(user_data.pop("password"))

    for field, value in user_data.items():
        setattr(user, field, value)

    return await UserRepository.update_user(session, user)
