from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_daily_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="👍 В офисе. Наланч нельзя", callback_data="vote_office_no_nalunch")],
            [InlineKeyboardButton(text="👨‍💻 В офисе. Наланч можно", callback_data="vote_office_nalunch")],
            [InlineKeyboardButton(text="👎 Не в офисе. Наланч можно", callback_data="vote_home_nalunch")],
            [InlineKeyboardButton(text="🗿 Не в офисе. Наланч нельзя", callback_data="vote_home_no_nalunch")]
        ]
    )

    return keyboard