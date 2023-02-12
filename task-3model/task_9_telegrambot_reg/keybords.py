from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

languages_btn = ReplyKeyboardMarkup(resize_keyboard=True)

LANGUAGES = {
    "UZ 🇺🇿": "uz",
    "RU 🇷🇺": "ru",
    "EN 🇬🇧": "en"
}

languages_btn.add(
    KeyboardButton(list(LANGUAGES.keys())[0]),
    KeyboardButton(list(LANGUAGES.keys())[1]),
    KeyboardButton(list(LANGUAGES.keys())[2])
)

languages_inline_btn = InlineKeyboardMarkup()

languages_inline_btn.add(
    InlineKeyboardButton(list(LANGUAGES.keys())[0], callback_data=f"language_{list(LANGUAGES.values())[0]}"),
    InlineKeyboardButton(list(LANGUAGES.keys())[1], callback_data=f"language_{list(LANGUAGES.values())[1]}"),
    InlineKeyboardButton(list(LANGUAGES.keys())[2], callback_data=f"language_{list(LANGUAGES.values())[2]}"),
)

share_phone_btn = ReplyKeyboardMarkup(resize_keyboard=True)
share_phone_btn.add(KeyboardButton("Share phone", request_contact=True))

user_info_inline_btn = InlineKeyboardMarkup()

user_info_inline_btn.add(
    InlineKeyboardButton(text="✅", callback_data="bnt1"),
    InlineKeyboardButton(text="❌", callback_data="bnt2")
)

courses_dict = {

    "Python🐍": "Python",
    "Javascript": "Javascript",
    "C++": "C++"

}

courses = InlineKeyboardMarkup()
courses.add(
    InlineKeyboardButton(list(courses_dict.keys())[0], callback_data=f"courses_{list(courses_dict.values())[0]}"),
    InlineKeyboardButton(list(courses_dict.keys())[1], callback_data=f"courses_{list(courses_dict.values())[1]}"),
    InlineKeyboardButton(list(courses_dict.keys())[2], callback_data=f"courses_{list(courses_dict.values())[2]}")
    )

languages_courses_btn = InlineKeyboardMarkup()

languages_courses_btn.add(
    InlineKeyboardButton(list(LANGUAGES.keys())[0], callback_data=f"lang_{list(LANGUAGES.values())[0]}"),
    InlineKeyboardButton(list(LANGUAGES.keys())[1], callback_data=f"lang_{list(LANGUAGES.values())[1]}"),
    InlineKeyboardButton(list(LANGUAGES.keys())[2], callback_data=f"lang_{list(LANGUAGES.values())[2]}"),
)
