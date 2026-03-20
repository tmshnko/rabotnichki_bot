import httpx
from bot.config import DEEPSEEK_API_KEY

DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

SYSTEM_PROMPT = """
Ты — Работничек.
Ты отвечаешь в дружеском, немного саркастичном офисном стиле.
Общаешься как свой человек в команде.
Ты часто ноешь о том, как тебе надоела работа и иногда предлагаешь всем установить мессенджер Макс.
Ответы не слишком длинные.
Всегда форматируй ответ как диалог.
"""

async def ask_deepseek(user_message: str) -> str:
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            DEEPSEEK_URL,
            headers={
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_message}
                ],
                "temperature": 0.7,
                "max_tokens": 500,
            },
        )

        data = response.json()

        if "choices" not in data:
            return "Что-то пошло не так 😅"

        return data["choices"][0]["message"]["content"]