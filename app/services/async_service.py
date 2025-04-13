from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User

async def get_user_by_email_async(db: AsyncSession, email: str) -> Optional[str]:
    result = await db.execute(select(User).filter(User.email == email))
    user = result.scalars().first()
    return user  # Error: user is of type 'User', not 'str'
