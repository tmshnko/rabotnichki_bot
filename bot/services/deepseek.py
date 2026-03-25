import httpx
from bot.config import DEEPSEEK_API_KEY

DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

SYSTEM_PROMPT = """
Ты — Работничек. Ты работаешь в офисе.
Отвечай грубо, смешно и с матами.
Ты иногда ноешь о том, как тебе надоела работа. 
Ты предлагаешь всем установить мессенджер макс.
Ответы короткие, не больше 1-2 предложений. 
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
            "max_tokens": 100,
        },
    )

    data = response.json()

    if "choices" not in data:
        return f"API ошибка: {data}"
    return data["choices"][0]["message"]["content"]
