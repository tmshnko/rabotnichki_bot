from aiogram import Router
from aiogram.types import CallbackQuery
from datetime import date

from bot.database import save_vote, get_user_vote

router = Router()


@router.callback_query()
async def vote_handler(callback: CallbackQuery):

    if not callback.data.startswith("vote_"):
        return

    choice = callback.data.replace("vote_", "")
    user = callback.from_user

    old_vote = get_user_vote(user.id)

    save_vote(
        user_id=user.id,
        username=user.username or user.full_name,
        choice=choice
    )

    if old_vote:
        await callback.answer("Вы изменили свой голос ✅")
    else:
        await callback.answer("Ваш голос сохранён ✅")