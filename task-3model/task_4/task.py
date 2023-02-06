from tkinter import *

windows = Tk()
windows['bg'] = '#fafafa'
windows.title("P10 git narsala uchib ketti")
# windows.wm_attributes('-alpha', 10)
windows.geometry("500x400")
windows.resizable(width=False, height=False)
# # label = Label(windows, text="hellow word")
# # text.place(x=10, y=10)
# label_name = Label(windows, text="You name: ")
# label_name.grid(row=0, column=0)
#
# new_entr = Entry(windows, width=20)
# new_entr.grid(row=0, column=1)
ful_name_label = Label(windows, text="Your name: ")
ful_name_label.place(x=100, y=10)
ful_name = Entry(windows, width=20)
ful_name.place(x=180, y=10)

emil = Label(windows, text="Email: ")
emil.place(x=100, y=40)
emil = Entry(windows, width=20)
emil.place(x=180, y=40)

dob = Label(windows, text="  DOB: ")
dob.place(x=100, y=70)
dob = Entry(windows, width=20)
dob.place(x=180, y=70)

gender = Label(windows, text="Gender: ")
gender.place(x=100, y=100)
gender = Entry(windows, width=20)
gender.place(x=180, y=100)

phone = Label(windows, text="Phone: ")
phone.place(x=100, y=130)
phone = Entry(windows, width=20)
phone.place(x=180, y=130)

course = Label(windows, text="Course: ")
course.place(x=100, y=130)
course = Entry(windows, width=20)
course.place(x=180, y=130)

if __name__ == "__main__":
    windows.mainloop()






