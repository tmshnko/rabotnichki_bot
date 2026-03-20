import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))
TEST_CHAT_ID = int(os.getenv("TEST_CHAT_ID"))
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

DAILY_TEXT = """
Ну че, кто в офис, братва?

👍 - буду в офисе, наланч не дам
👨‍💻 - буду в офисе, наланч можно брать
👎 - не в офисе, наланч МОЖНО 
🗿 - не в офисе, наланч НЕЛЬЗЯ
🍓 - я работаю в 2гис лол
"""
