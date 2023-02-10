import json
from datetime import datetime
import re
from googletrans import Translator, LANGUAGES
from googletrans import *

from Krili_Uzbek import to_cyrillic, to_latin
from telebot.types import BotCommand
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import telebot

from weather_func import WeatherManager

# Python_p10
BOT_TOKEN = ''

bot = telebot.TeleBot(BOT_TOKEN)
language = LANGUAGES
language_list = list(language.values())
trasnlator = Translator()


# /start
@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    bot.send_message(chat_id, f"Assalomu alaykum, {user.first_name}")


@bot.message_handler(commands=["translator"])
def google_translator(pere):
    chat_id = pere.chat.id
    bot.send_message(chat_id, "Assalomu alaykum Men Googletrans Man So'z Kiriting:")
    bot.register_next_step_handler(pere, perev)


perevod = []


def perev(pere):
    chat_id = pere.chat.id
    perevod.append(pere.text)
    x = trasnlator.detect(pere.text)
    perevod.append(x.lang)
    bot.send_message(chat_id, f"Siz Kiritgan So'zni Tili:\t{x.lang}")
    days_btn = ReplyKeyboardMarkup(row_width=True)
    for lang in language_list:
        formatted_day = lang
        days_btn.add(
            KeyboardButton(formatted_day))
    msg = "Qaysi tilga Tanlang:"
    bot.send_message(pere.chat.id, msg, parse_mode="html", reply_markup=days_btn)
    bot.register_next_step_handler(pere, perevedchi)


def perevedchi(message):
    chat_id = message.chat.id
    x = trasnlator.translate(perevod[0], src=perevod[1], dest=message.text)
    bot.send_message(chat_id, f"Siz Kiritgan So'zni Tili perevodi-->\t{x.text}")


# @bot.message_handler(commands=["weather"])
# def weather_hand(message):
#     chat_id = message.chat.id
#     bot.send_message(chat_id, "Shahar nomi  Kiriting:")
#     bot.register_next_step_handler(message, weather_handler)
#
#
#
#
# def weather_handler(message):
#     today = datetime.now()
#     weather_data = WeatherManager(message.text).get_daily_temperature()
#     with open('weather.json', 'w') as f:
#         json.dump(weather_data, f, indent=2)
#     today_weather = None
#     for day_weather in weather_data:
#         day_date = datetime.strptime(day_weather.get("day"), "%Y.%m.%d")
#         if day_date.date() == today.date():
#             today_weather = day_weather
#     res = [day_temp.get("day") for day_temp in weather_data]
#     days_btn = ReplyKeyboardMarkup(row_width=True)
#     for day in res:
#         formatted_day = datetime.strptime(day, "%Y.%m.%d").strftime("%b %d %Y")
#         days_btn.add(
#             KeyboardButton(formatted_day))
#     msg = f"<b>Bugungi ob-havo:</b>\n\n" \
#           f"<i>Harorat:</i> {today_weather.get('average_temperature')}"
#     bot.send_message(message.chat.id, msg, parse_mode="html", reply_markup=days_btn)
#     bot.register_next_step_handler(message, day_weather_message)
#
#
# def day_weather_message(message):
#     date_msg = message.text
#     date = datetime.strptime(date_msg, "%b %d %Y")
#     with open('weather.json') as f:
#         weather_data = json.load(f)
#         weather = None
#         for day_weather in weather_data:
#             day_date = datetime.strptime(day_weather.get("day"), "%Y.%m.%d")
#             if day_date.date() == date.date():
#                 weather = day_weather
#         msg = f"<b>{date_msg} ob-havo:</b>\n\n" \
#               f"<i>Harorat:</i> {weather.get('average_temperature')}"
#         bot.reply_to(message, msg, parse_mode="html")


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/translator", "Google_translator")
    ]


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    print("ishlayapti.......")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
