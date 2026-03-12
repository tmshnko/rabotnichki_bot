from aiogram import Router
from aiogram.types import CallbackQuery
from datetime import date

from bot.database import save_vote, get_today_votes, get_daily_message
from bot.utils import build_text
from bot.keyboards import get_daily_keyboard

router = Router()


@router.callback_query()
async def vote_handler(callback: CallbackQuery):

    if not callback.data.startswith("vote_"):
        return

    choice = callback.data
    user = callback.from_user

    save_vote(
        user_id=user.id,
        username=user.username or user.full_name,
        choice=choice
    )

    # Получаем все голоса
    votes = get_today_votes()

    # Формируем новый текст
    new_text = build_text(votes)

    # Получаем сообщение дня
    daily_msg = get_daily_message()

    if daily_msg:
        chat_id, message_id = daily_msg

        await callback.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=new_text,
            reply_markup=get_daily_keyboard()
        )

    await callback.answer("ну ок")