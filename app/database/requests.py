from app.database.models import async_session
from app.database.models import User, Performer, Song
from sqlalchemy import select

async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def get_performers():
    async with async_session() as session:
        return await session.scalars(select(Performer))

async def get_perf_song(performer_id):
    async with async_session() as session:
        return await session.scalars(select(Song).where(Song.performer == performer_id))