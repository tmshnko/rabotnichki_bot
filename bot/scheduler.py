from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from .config import CHAT_ID, DAILY_TEXT, TEST_CHAT_ID
from .keyboards import get_daily_keyboard
import pytz

def setup_scheduler(bot: Bot):
    timezone = pytz.timezone("Europe/Moscow")

    scheduler = AsyncIOScheduler(timezone=timezone)

    async def send_daily_message():
        await bot.send_message(
            chat_id=CHAT_ID,
            text=DAILY_TEXT
        )

    async def send_daily_message_new():
        await bot.send_message(
            chat_id=TEST_CHAT_ID,
            text="Ну че как братва?",
            reply_markup=get_daily_keyboard()
        )

    scheduler.add_job(send_daily_message, "cron", hour=8, minute=0, day_of_week='mon-fri')
    scheduler.add_job(send_daily_message_new, "cron", hour=13, minute=54)

    scheduler.start()

    return scheduler
