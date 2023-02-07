from datetime import date, datetime, timezone
import json
import time
import tkinter
from tkinter import Label, Entry, Button, Text, END, ttk
import requests

"vazifada vaqtni olish uchun time, " \
"o'rtacha harorat olish uchun daily dan temperatureAvg, " \
"hourly uchun temperature keydan olamiz"


def convert_to_datetime(date_str):
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")


#
def get_obhavo():
    time = {}
    daily = {}
    hourly = {}
    time2 = {}
    APIKEY = 'f8b2d053619466269dabba1c9a88f443'
    url = f"https://api.tomorrow.io/v4/weather/forecast?location=newyork&apikey={APIKEY}"
    # headers = {"accept": "application/json"}
    response = requests.get(url).json()
    print(response)
    # with open('time.json', 'r') as file:
    #     data = datetime.now()
    #     time.update(json.load(file))

get_obhavo()

    # windows = tkinter.Tk()
    # windows.title("Obhavo")
    # windows.geometry('500x600')
    # text_label = Label(windows, text="So'z kiriting", bg="red", font=20)
    # text_label.place(x=0, y=10)
    # text_entry = Entry(windows, width=20, font=20)
    # text_entry.pack()
    # text_entry.focus()
    #
    # weter = Label(windows, text="", font=20)
    # weter.place(x=0, y=150)
    #
    # resulat = Label(windows, text="", bg="red", font=20)
    # resulat.place(x=0, y=90)
    #
    # buttton = Button(windows, text="Enter", padx=20, pady=10, bg="green", command=get_obhavo)
    # buttton.place(x=210, y=40)
    #
    # if __name__ == "__main__":
    #     windows.mainloop()
