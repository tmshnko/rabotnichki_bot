import asyncio
from aiogram import Bot, Dispatcher
from .config import BOT_TOKEN
from .handlers import basic, votes
from .scheduler import setup_scheduler
from .database import init_db


async def main():
    init_db()
    bot = Bot(token=BOT_TOKEN, validate_token=False)
    dp = Dispatcher()

    dp.include_router(basic.router)
    dp.include_router(votes.router)

    # Настройка планировщика
    scheduler = setup_scheduler(bot)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())