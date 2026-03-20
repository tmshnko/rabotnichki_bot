from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from .config import CHAT_ID, DAILY_TEXT,  TEST_CHAT_ID
from .keyboards import get_daily_keyboard
from .database import save_daily_message
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
        msg = await bot.send_message(
            chat_id=TEST_CHAT_ID,
            text="Ну че как братва?",
            parse_mode='HTML',
            reply_markup=get_daily_keyboard()
        )
        save_daily_message(msg.chat.id, msg.message_id)

    scheduler.add_job(send_daily_message_new, "cron", hour=8, minute=0, day_of_week='mon-fri')
    scheduler.add_job(send_daily_message_new, "cron", hour=1, minute=55)

    scheduler.start()

    return scheduler
