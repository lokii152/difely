import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from app.handlers import router_h
from app.registration import router_reg
from app.auth import router_auth
from app.database.models import async_main


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    await async_main()
    dp.include_routers(router_h, router_reg, router_auth)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
