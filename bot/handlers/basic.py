from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.database import get_today_votes, save_vote, get_user_vote
from bot.utils import build_text_lunch, text_left_lunches

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("я работничек хуев")

@router.message(Command("lunch"))
async def lunch_handler(message: Message):
    votes = get_today_votes()
    text = build_text_lunch(votes)

    await message.answer(text, parse_mode='HTML')

@router.message(Command("take"))
async def take_lunch_handler(message:Message):
    user = message.text.replace('/take ', '').replace('@', '').strip()

    info = get_today_votes() 
    users_with_lunch = []
    for username, vote in info:
        if 'no_nalunch' not in vote:
            users_with_lunch.append(username)

    if user not in users_with_lunch: 
        await message.answer(f"у {user} нельзя взять наланч")
        return

    current_choice = get_user_vote(user)

    if 'office' in current_choice:
        new_choice = 'vote_office_no_lunch'
    else:
        new_choice = 'vote_home_no_lunch'

    save_vote(
        username=user,
        choice=new_choice
    )

    votes = get_today_votes() 
    text = text_left_lunches(votes, user)

    await message.answer(text, parse_mode='HTML')