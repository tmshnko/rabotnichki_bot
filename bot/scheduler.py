from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from .config import CHAT_ID, DAILY_TEXT
import pytz

def setup_scheduler(bot: Bot):

    timezone = pytz.timezone("Europe/Moscow")
    scheduler = AsyncIOScheduler(timezone=timezone)

    async def send_daily_message():
        await bot.send_message(
            chat_id=CHAT_ID,
            text=DAILY_TEXT
        )

    scheduler.add_job(send_daily_message, "cron", hour=17, minute=0)

    scheduler.start()