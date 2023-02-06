from datetime import date, datetime,timezone
import json
import time
import tkinter
from tkinter import Label, Entry, Button, Text, END, ttk
import requests
from timezonefinder import TimezoneFinder

#
# def get_obhavo():
#     url = "http://api.openweathermap.org/data/2.5/weather?q=Tashkent&APPID=bc10a5bdc3a7549e14a0b0df43d103d0"
#     response = requests.get(url).json()
#     print(response)
#     # ob-havo malumaotini olsh
#     condition = response['main']
#     print()
#     # xarorati olish
#     temp = int(response['main']['temp'] - 273.15)
#     print(temp)
#     temp_min = int(response['main']['temp_min'] - 273.15)
#     temp_max = int(response['main']['temp_max'] - 273.15)
#     # pressure Bu bosimni beradi
#     pressure = response['main']['pressure']
#     # humidity Bu Namlikni Beradi
#     humidity = response['main']['humidity']
#     # sunrise = time.strftime("%I:%M:%S", time.gmtime(response['sys']['sunrise'] - 21600))
#     # print(sunrise)
#     # sunset = time.strftime("%I:%M:%S", time.gmtime(response['sys']['sunset'] - 21600))
#     # print(sunset)
#     # weter.configure(text=temp)
#     data=datetime.now(timezone(response['timezone']))
#     print(data)
#
#
# get_obhavo()

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
# import requests
#
# APIKEY = 'ZQ48KUlOHW4H7bnsvgNlF02Z06kwKvoB'
# url = f"https://api.tomorrow.io/v4/weather/forecast?location=newyork&apikey={APIKEY}"
#
# headers = {"accept": "application/json"}
#
# response = requests.get(url, headers=headers).json()
# print(response)
url = f"https://api.exchangerate-api.com/v4/latest/{combo1.get()}"
        response = requests.get(url)
        data = response.json()
        result = data['rates'][combo2.get()]
        result = float(result) * float(entry1.get(1.0, tk.END))