import logging

from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.user import User
from src.usecase.port.repositories import Repository

logger = logging.getLogger(__name__)


class Service:
    def __init__(self, repo: Repository) -> None:
        self.repo = repo

    async def create_user(self, user: User, session: AsyncSession) -> User:
        created = await self.repo.create_user(user, session)
        logger.info("User created with ID: %s", created.id)
        return created
