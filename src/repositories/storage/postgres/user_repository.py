from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.user import User
from src.repositories.storage.map.user import map_to_domain, map_to_model


class SQLAlchemyUserRepository:
    async def create_user(self, user: User, session: AsyncSession) -> User:
        model = map_to_model(user)
        session.add(model)
        await session.commit()
        await session.refresh(model)
        return map_to_domain(model)
