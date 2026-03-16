from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.database import get_today_votes
from bot.utils import build_text_lunch

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
    user=message.from_user 
    await message.answer(message.text)