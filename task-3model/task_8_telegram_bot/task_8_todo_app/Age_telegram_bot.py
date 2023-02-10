from datetime import datetime

from telebot.types import BotCommand
import telebot

# P10_telgram_bot_Task_8
BOT_TOKEN = "6299474557:AAHuXfxGhNzhpJJ_GggTCaiNVu8OGc7NfFc"
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    bot.send_message(chat_id, f"Assalomu alaykum, {user.first_name}")


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


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/age", "Age_calculatotor")
    ]


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    print("ishlayapti.......")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
