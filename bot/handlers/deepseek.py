from aiogram import Router
from aiogram.types import Message
from bot.services.deepseek import ask_deepseek

router = Router()


@router.message()
async def deepseek_handler(message: Message):

    if not message.text:
        return

    text = message.text.strip()

    # Проверяем начинается ли с "работничек"
    if not text.lower().startswith("работничек"):
        return

    # Убираем ключевое слово
    user_prompt = text[len("работничек"):].strip()

    if not user_prompt:
        await message.answer("Слушаю тебя 👀")
        return

    response = await ask_deepseek(user_prompt)

    await message.answer(response)