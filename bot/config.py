import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

DAILY_TEXT = """
Ну че, кто в офис, братва?

👍 - буду в офисе, наланч не дам
👨‍💻 - буду в офисе, наланч можно брать
👎 - не в офисе, наланч МОЖНО 
🗿 - не в офисе, наланч НЕЛЬЗЯ
🍓 - я работаю в 2гис лол
"""
