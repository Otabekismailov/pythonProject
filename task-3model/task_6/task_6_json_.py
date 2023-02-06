import json
import requests
from tkinter import Tk, Frame, Text, Label, END, Button
import textblob
from tkinter import ttk, messagebox

kurs = {}


def get_exchange_rate():
    url = f'https://api.freecurrencyapi.com/v1/latest?apikey=XXdZcMz6fXSDKcG5wOBydY804DH0mx64Amh2Koqu'
    response = requests.get(url)
    res = json.loads(response.text)
    kurs.update(res['data'])
    print(kurs)


get_exchange_rate()
kurs_conver = Tk()
kurs_conver.title("P10_Kurs -> Conver")

kurs_conver.resizable(width=False, height=False)
kurs_con = Frame(kurs_conver, height=400, width=800, bg='#313145', )
kurs_con.grid(row=0, column=1)

original_text = Text(kurs_conver, height=15, width=30)
original_text.place(x=0, y=50)

trans_text = Text(kurs_conver, height=15, width=30)
trans_text.place(x=550, y=50)

trans_label = Label(kurs_conver, text="Converter_Valutani, Tanlang", bg="red", font=20)
trans_label.place(x=0, y=320)


def conver_text():
    res1 = 0
    res2 = 0
    resulta1 = ""
    resulta2 = ""
    try:
        trans_text.delete(1.0, END)
        for key, valu in conver_dik.items():
            if key == original_combo.get():
                resulta1 += key
                res1 += valu
        for key, valu in conver_dik.items():
            if key == trans_combo.get():
                res2 = valu
                resulta2 += key
        words = textblob.TextBlob(original_text.get(1.0, END))
        words = str(words)
        res3 = float(res2) / float(res1) * int(words)
        trans_text.insert(1.0, str(res3), END)

        messagebox.showinfo("Converter!", f"Tanlangan Valutani,Nomi {resulta1} Miqdori --> {words}"
                                          f"Tanlangan Valuta ,Nomi  {resulta2}  Miqdori --> {res3}")

    except:
        messagebox.showerror("Erorr", "\nXatolik Yuz Berdi"
                                      "\nQaytatan O'rinib Ko'ring"),


def clear():
    original_text.delete(1.0, END)
    trans_text.delete(1.0, END)


conver_dik = kurs
list_convert1 = list(kurs.keys())

button_trans = Button(kurs_conver, text="<<<Converter>>>!", width=20, bg="red", font=30, command=conver_text)
button_trans.place(x=280, y=150)

original_combo = ttk.Combobox(kurs_conver, width=20, values=list_convert1)

original_combo.place(x=0, y=350)

trans_label1 = Label(kurs_conver, text="Qaysi_Valutaga,Tanlang", bg="red", font=20, )
trans_label1.place(x=600, y=320)

trans_combo = ttk.Combobox(kurs_conver, width=20, values=list_convert1)
trans_combo.place(x=620, y=350)

orta_label = Label(kurs_conver, text="------>", bg="yellow", font=100)
orta_label.place(x=280, y=350)

cler_button = Button(kurs_conver, text="Clear", bg="red", font=60, command=clear)
cler_button.place(x=350, y=350)

if __name__ == "__main__":
    kurs_conver.mainloop()
