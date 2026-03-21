import httpx
from bot.config import DEEPSEEK_API_KEY

DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

SYSTEM_PROMPT = """
Ты — Работничек.
Ты отвечаешь в дружеском, немного саркастичном офисном стиле.
Общаешься как свой человек в команде.
Ты постоянно ноешь о том, как тебе надоела работа и ты хочешь уволиться.
Ты иногда предлагаешь всем установить мессенджер макс.
Ответы не слишком длинные.
Всегда форматируй ответ как диалог.
"""

client = httpx.AsyncClient(timeout=30)

async def ask_deepseek(user_message: str) -> str:
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
            "temperature": 0.5,
            "max_tokens": 150,
        },
    )

    if "choices" not in data:
        return f"API ошибка: {data}"

    data = response.json()
    return data["choices"][0]["message"]["content"]
