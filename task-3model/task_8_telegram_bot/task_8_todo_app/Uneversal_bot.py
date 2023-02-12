import json
from datetime import datetime
from Krili_Uzbek import to_cyrillic, to_latin
from telebot.types import BotCommand
from googletrans import LANGUAGES
from googletrans import *
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import telebot

from weather_func import WeatherManager

#
BOT_TOKEN = "6298984262:AAHoLF-7c6hPzx1VxzRXC12AOI7N1WjCuQg"

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


@bot.message_handler(commands=["krillik_uzbek"])
def krilik_Uzbek(pere):
    chat_id = pere.chat.id
    bot.send_message(chat_id, "So'z Kiriting:")
    bot.register_next_step_handler(pere, perev)


def perev(pere):
    try:
        chat_id = pere.chat.id
        if pere.text.isascii():
            bot.send_message(chat_id, f"Siz kiritgan So'z Krilcha Ko'rinishi {to_cyrillic(pere.text)}")

        else:
            bot.send_message(chat_id, f"Siz kiritgan So'z Lotincha Ko'rinishi {to_latin(pere.text)}")

    except Exception as e:
        bot.reply_to(pere, 'xatolik')


@bot.message_handler(commands=["age"])
def age(message):
    chat_id = message.chat.id
    print(message.text)
    bot.send_message(chat_id, "Yilingizni Kiriting:")
    bot.register_next_step_handler(message, calculateage)


def calculateage(message):
    chat_id = message.chat.id
    current_year = datetime.now().year
    data_day = datetime.strptime(message.text, "%Y")
    your_age = current_year - data_day.year
    bot.send_message(chat_id, f"Sizni Yoshingiz:\t{your_age}")


@bot.message_handler(commands=["weather"])
def weather_hand(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Shahar nomi  Kiriting:")
    bot.register_next_step_handler(message, weather_handler)


def weather_handler(message):
    today = datetime.now()
    weather_data = WeatherManager(message.text).get_daily_temperature()
    with open('weather.json', 'w') as f:
        json.dump(weather_data, f, indent=2)
    today_weather = None
    for day_weather in weather_data:
        day_date = datetime.strptime(day_weather.get("day"), "%Y.%m.%d")
        if day_date.date() == today.date():
            today_weather = day_weather
    res = [day_temp.get("day") for day_temp in weather_data]
    days_btn = ReplyKeyboardMarkup(row_width=True)
    for day in res:
        formatted_day = datetime.strptime(day, "%Y.%m.%d").strftime("%b %d %Y")
        days_btn.add(
            KeyboardButton(formatted_day))
    msg = f"<b>Bugungi ob-havo:</b>\n\n" \
          f"<i>Harorat:</i> {today_weather.get('average_temperature')}"
    bot.send_message(message.chat.id, msg, parse_mode="html", reply_markup=days_btn)
    bot.register_next_step_handler(message, day_weather_message)


def day_weather_message(message):
    date_msg = message.text
    date = datetime.strptime(date_msg, "%b %d %Y")
    with open('weather.json') as f:
        weather_data = json.load(f)
        weather = None
        for day_weather in weather_data:
            day_date = datetime.strptime(day_weather.get("day"), "%Y.%m.%d")
            if day_date.date() == date.date():
                weather = day_weather
        msg = f"<b>{date_msg} ob-havo:</b>\n\n" \
              f"<i>Harorat:</i> {weather.get('average_temperature')}"
        bot.reply_to(message, msg, parse_mode="html")


@bot.message_handler(commands=["translator"])
def google_translator(pere_vodchik):
    chat_id = pere_vodchik.chat.id
    bot.send_message(chat_id, "Assalomu alaykum Men Googletrans Man So'z Kiriting:")
    bot.register_next_step_handler(pere_vodchik, google)


perevod = []


def google(pere_vodchik):
    chat_id = pere_vodchik.chat.id
    perevod.append(pere_vodchik.text)
    x = trasnlator.detect(pere_vodchik.text)
    perevod.append(x.lang)
    bot.send_message(chat_id, f"Siz Kiritgan So'zni Tili:\t{x.lang}")
    days_btn = ReplyKeyboardMarkup(row_width=True)
    for lang in language_list:
        formatted_day = lang
        days_btn.add(
            KeyboardButton(formatted_day))
    msg = "Qaysi tilga Tanlang:"
    bot.send_message(pere_vodchik.chat.id, msg, parse_mode="html", reply_markup=days_btn)
    bot.register_next_step_handler(pere_vodchik, perevedchi)


def perevedchi(message):
    chat_id = message.chat.id
    x = trasnlator.translate(perevod[0], src=perevod[1], dest=message.text)
    bot.send_message(chat_id, f"Siz Kiritgan So'zni Tili perevodi-->\t{x.text}")


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/krillik_uzbek", "Krilik_Uzbek"),
        BotCommand("/age", "Age_calculator"),
        BotCommand("/weather", "Weather"),
        BotCommand("/translator", "Google_translator")
    ]


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    print("ishlayapti.......")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
