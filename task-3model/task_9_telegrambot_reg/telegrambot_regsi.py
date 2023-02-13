import csv
import json
import os
from datetime import datetime

import telebot
from environs import Env
from telebot import custom_filters
from telebot.storage import StateMemoryStorage
from telebot.types import BotCommand, ReplyKeyboardRemove

from keybords import languages_inline_btn, share_phone_btn, user_info_inline_btn, courses, languages_courses_btn
from messages import messages
from states import StudentRegistrationForm
from task import Chat, Task
from utils import get_fullname, write_row_to_csv, get_language_code_by_chat_id

# env = Env()
# env.read_env(".")

BOT_TOKEN = '5933705026:AAGq4F95_Fg1Aka0J2MNwvHkw0Rbcn1tAb8'

state_storage = StateMemoryStorage()

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html", state_storage=state_storage)


# /start


@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    fullname = get_fullname(user.first_name, user.last_name)
    bot.send_message(chat_id, f"Assalomu alaykum, {fullname}", reply_markup=languages_inline_btn)


@bot.callback_query_handler(lambda call: call.data.startswith("language_"))
def set_language_query_handler(call):
    message = call.message
    lang_code = call.data.split("_")[1]
    chat = message.chat
    new_chat = Chat(
        chat.id,
        get_fullname(chat.first_name, chat.last_name),
        lang_code
    )
    write_row_to_csv(
        "chats.csv",
        list(new_chat.get_attrs_as_dict().keys()),
        new_chat.get_attrs_as_dict()
    )
    bot.delete_message(chat.id, message.id)
    bot.send_message(chat.id, messages[lang_code].get("add_task"))


@bot.message_handler(commands=["register"])
def register_student_handler(message):
    bot.send_message(message.chat.id, "Ismingizni kiriting:")
    bot.set_state(message.from_user.id, StudentRegistrationForm.first_name, message.chat.id)
    # bot.register_next_step_handler(message, first_name_get)


@bot.message_handler(state=StudentRegistrationForm.first_name)
def first_name_get(message):
    bot.send_message(message.chat.id, 'Familyangizni kiriting:')
    bot.set_state(message.from_user.id, StudentRegistrationForm.last_name, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['first_name'] = message.text


@bot.message_handler(state=StudentRegistrationForm.last_name)
def last_name_get(message):
    bot.send_message(message.chat.id, 'Telefon raqaminingizni yuboring:', reply_markup=share_phone_btn)
    bot.set_state(message.from_user.id, StudentRegistrationForm.phone, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['last_name'] = message.text


@bot.message_handler(state=StudentRegistrationForm.phone, content_types=["contact"])
def phone_get(message):
    bot.send_message(message.chat.id, 'Yoshingizni kiriting:', reply_markup=ReplyKeyboardRemove())
    bot.set_state(message.from_user.id, StudentRegistrationForm.age, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['phone'] = message.contact.phone_number


@bot.message_handler(state=StudentRegistrationForm.age)
def age_get(message):
    bot.send_message(message.chat.id, 'Tilni kiriting:', reply_markup=languages_courses_btn)
    bot.set_state(message.from_user.id, StudentRegistrationForm.language, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['age'] = message.text


@bot.message_handler(state=StudentRegistrationForm.language)
def leng_get(message):
    bot.set_state(message.from_user.id, StudentRegistrationForm.course, message.chat.id)


@bot.callback_query_handler(lambda call: call.data.startswith("lang_"))
def set_language2_query_handler(call):
    message = call.message
    lang_code = call.data.split("_")[1]
    bot.set_state(call.from_user.id, StudentRegistrationForm.language, message.chat.id)
    with bot.retrieve_data(call.from_user.id, message.chat.id) as data:
        data['language'] = lang_code
        bot.send_message(message.chat.id, 'Kursni kiriting:', reply_markup=courses)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Ma'lumot qabul qilindi")


user_list = []


@bot.message_handler(state=StudentRegistrationForm.course)
def course_get(message):
    bot.set_state(message.from_user.id, StudentRegistrationForm.course, message.chat.id)


@bot.callback_query_handler(lambda call: call.data.startswith("courses_"))
def set_language3_query_handler(call):
    message = call.message
    lang_courses = call.data.split("_")[1]
    with bot.retrieve_data(call.from_user.id, message.chat.id) as data:
        data['course'] = lang_courses
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Ma'lumot qabul qilindi")

        user = {
            "user_id": message.chat.id,
            "Fullname": f"{data.get('first_name')} {data.get('last_name')}",
            "Phone": data.get('phone'),
            "Age": data.get('age'),
            "Language": data.get('language'),
            "Course": data.get('course')
        }
        user_list.append(user)
        msg = "Quyidagi ma'lumotlar qa'bul qilindi:\n"
        msg += f"Fullname: {data.get('first_name')} {data.get('last_name')}\n"
        msg += f"Phone: {data.get('phone')}\n"
        msg += f"Age: {data.get('age')}\n"
        msg += f"Language: {data.get('language')}\n"
        msg += f"Course: {data.get('course')}\n"
        msg += "Ma'lumotni tasdiqlaysizmi?🧐"
        bot.send_message(message.chat.id, msg, parse_mode="html", reply_markup=user_info_inline_btn)
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.callback_query_handler(lambda call: call.data)
def add_user_info(call):
    if call.data == "bnt1":
        headr = ["user_id", "Fullname", "Phone", "Age", "Language", "Course"]
        with open('user_informesion.csv', "a+", newline='\n') as file:
            csv_writer = csv.DictWriter(file, fieldnames=headr)
            csv_writer.writeheader()
            csv_writer.writerows(user_list)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Ma'lumot qabul qilindi")


    elif call.data == "bnt2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Qayta Urinib Ko'ring /register")
    bot.delete_state(call.from_user.id, call.message.chat.id)


# bot.delete_state(call.from_user.id, call.message.chat.id)


@bot.message_handler(commands=["add"])
def add_task_handler(message):
    chat_id = message.chat.id
    lang_code = get_language_code_by_chat_id(chat_id, "chats.csv")
    msg = messages[lang_code].get("send_task")
    bot.send_message(message.chat.id, msg)

    bot.register_next_step_handler(message, get_task_handler)


@bot.message_handler(content_types=["text"])
def get_task_handler(message):
    chat_id = message.chat.id
    if message.content_type != "text":
        bot.send_message(chat_id, "Invalid format.")

    new_task = Task(chat_id, message.text, datetime.now())
    write_row_to_csv(
        "tasks.csv",
        list(new_task.get_attrs_as_dict().keys()),
        new_task.get_attrs_as_dict()
    )

    bot.send_message(chat_id, "Add successfully.")


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/add", "Add new task"),
        BotCommand("/register", "Register student")
    ]


bot.add_custom_filter(custom_filters.StateFilter(bot))

if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
