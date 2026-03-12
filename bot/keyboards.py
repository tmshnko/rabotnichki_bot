from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_daily_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="👍 В офисе. Наланч нельзя", callback_data="office_no_nalunch")],
            [InlineKeyboardButton(text="👨‍💻 В офисе. Наланч можно", callback_data="office_nalunch")],
            [InlineKeyboardButton(text="👎 Не в офисе. Наланч можно", callback_data="home_nalunch")],
            [InlineKeyboardButton(text="🗿 Не в офисе. Наланч нельзя", callback_data="home_no_nalunch")]
        ]
    )

    return keyboard